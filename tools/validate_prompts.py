#!/usr/bin/env python3
"""Validator for legal-ai-prompts repo.

Run with: python tools/validate_prompts.py
Exits non-zero on any error. Prints a diagnostic per error.

Requires: pip install pyyaml jsonschema
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as e:
    print(f"[FATAL] Missing dependency: {e}. pip install pyyaml jsonschema", file=sys.stderr)
    sys.exit(2)


ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
PACKS_DIR = ROOT / "packs"
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)
CANONICAL_ID_RE = re.compile(r"^LP-V[1-8]-[A-Z]{2,4}-\d{4}$")
PLACEHOLDER_RE = re.compile(r"\[([^\[\]]+)\]")
VALID_PLACEHOLDER_RE = re.compile(r"^[A-Z][A-Z0-9 _/\-&]{1,}$")
TOMBSTONE_FILE = SCHEMAS_DIR / "tombstones.json"


class ValidationErrors:
    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def ok(self) -> bool:
        return not self.errors

    def report(self) -> None:
        for e in self.errors:
            print(f"[ERROR] {e}", file=sys.stderr)


def load_schemas(errs: ValidationErrors) -> dict[str, dict]:
    """Load and validate all JSON Schemas in schemas/ directory."""
    schemas: dict[str, dict] = {}
    seen_ids: set[str] = set()
    for path in sorted(SCHEMAS_DIR.glob("*.schema.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errs.add(str(path.relative_to(ROOT)), f"invalid JSON: {e}")
            continue
        if data.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errs.add(str(path.relative_to(ROOT)), "missing or wrong $schema (expected draft 2020-12)")
        sid = data.get("$id")
        if not sid:
            errs.add(str(path.relative_to(ROOT)), "missing $id")
        elif sid in seen_ids:
            errs.add(str(path.relative_to(ROOT)), f"duplicate $id: {sid}")
        else:
            seen_ids.add(sid)
        schemas[path.name] = data
    return schemas


def validate_front_matter(
    fm_schema: dict, fm: dict, where: str, errs: ValidationErrors
) -> None:
    """Validate a parsed front-matter dict against the front-matter schema."""
    validator = Draft202012Validator(fm_schema)
    for err in validator.iter_errors(fm):
        errs.add(where, f"front matter: {err.message}")


def walk_prompt_files() -> list[Path]:
    """Collect all markdown files in volume-*/ and quick-start-packs/."""
    paths: list[Path] = []
    for volume_dir in sorted(ROOT.glob("volume-*/")):
        paths.extend(sorted(volume_dir.glob("*.md")))
    qsp = ROOT / "quick-start-packs"
    if qsp.is_dir():
        paths.extend(sorted(qsp.glob("*.md")))
    return paths


def check_placeholders(body: str, where: str, errs: ValidationErrors) -> None:
    """Enforce [UPPERCASE_PLACEHOLDER] convention in pilot files."""
    # Strip fenced code blocks, inline code, markdown links, footnotes, checkboxes
    cleaned = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    cleaned = re.sub(r"`[^`\n]+`", "", cleaned)
    cleaned = re.sub(r"\[([^\[\]\n]+)\]\([^)]+\)", "", cleaned)
    cleaned = re.sub(r"\[\^[^\]]+\]", "", cleaned)
    cleaned = re.sub(r"\[[ xX]\]", "", cleaned)
    bad: set[str] = set()
    for m in PLACEHOLDER_RE.finditer(cleaned):
        token = m.group(1).strip()
        if not token or token.isdigit():
            continue
        if any(c.isupper() for c in token) and not VALID_PLACEHOLDER_RE.match(token):
            bad.add(token)
    if bad:
        sample = ", ".join(sorted(bad)[:5])
        errs.add(where, f"invalid placeholder token(s): {sample}")


def _has_cycle(graph: dict[str, list[str]]) -> bool:
    """Detect cycles in a directed graph via DFS colouring."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in graph}

    def visit(n: str) -> bool:
        if color[n] == GRAY:
            return True
        if color[n] == BLACK:
            return False
        color[n] = GRAY
        for m in graph.get(n, []):
            if visit(m):
                return True
        color[n] = BLACK
        return False

    return any(visit(n) for n in list(graph))


def main() -> int:
    errs = ValidationErrors()

    # --- 1. Validate schemas ---
    schemas = load_schemas(errs)
    fm_schema = schemas.get("prompt.frontmatter.schema.json")
    pack_schema = schemas.get("pack.schema.json")
    if fm_schema is None:
        errs.add("schemas/", "prompt.frontmatter.schema.json missing")
    if pack_schema is None:
        errs.add("schemas/", "pack.schema.json missing")

    # --- 2. Validate prompt files ---
    all_ids: dict[str, str] = {}  # id -> relative file path
    all_chains_to: list[tuple[str, str]] = []  # (source_id, referenced_id)
    tombstones: set[str] = set()
    if TOMBSTONE_FILE.exists():
        try:
            tombstones = set(
                json.loads(TOMBSTONE_FILE.read_text(encoding="utf-8")).get("ids", [])
            )
        except json.JSONDecodeError as e:
            errs.add(str(TOMBSTONE_FILE.relative_to(ROOT)), f"invalid JSON: {e}")

    for path in walk_prompt_files():
        rel = str(path.relative_to(ROOT))
        try:
            raw = path.read_bytes()
        except OSError as e:
            errs.add(rel, f"read error: {e}")
            continue

        # BOM check
        if raw.startswith(b"\xef\xbb\xbf"):
            errs.add(rel, "UTF-8 BOM not allowed")
            raw = raw[3:]

        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            errs.add(rel, f"not valid UTF-8: {e}")
            continue

        m = FRONT_MATTER_RE.match(content)
        if m:
            # --- File has front matter ---
            yaml_text = m.group(1)
            if "\t" in yaml_text:
                errs.add(rel, "tab character in front matter (use spaces)")
            try:
                fm = yaml.safe_load(yaml_text) or {}
            except yaml.YAMLError as e:
                errs.add(rel, f"front matter YAML error: {e}")
                fm = None

            if fm is not None and fm_schema is not None:
                validate_front_matter(fm_schema, fm, rel, errs)

                pid = fm.get("id") if isinstance(fm, dict) else None
                if isinstance(pid, str):
                    if pid in all_ids:
                        errs.add(rel, f"duplicate id {pid} (also in {all_ids[pid]})")
                    else:
                        all_ids[pid] = rel

                if isinstance(fm, dict):
                    for ref in fm.get("chains_to", []) or []:
                        all_chains_to.append((pid or rel, ref))

                    out_s = fm.get("output_schema")
                    if isinstance(out_s, str):
                        if not (ROOT / out_s).is_file():
                            errs.add(rel, f"output_schema not found: {out_s}")

            body = content[m.end():]

            # Title match check
            first_h1 = re.search(r"^\s*#\s+(.+)$", body, flags=re.MULTILINE)
            if first_h1 and isinstance(fm, dict):
                expected = fm.get("title", "").strip()
                actual = first_h1.group(1).strip()
                if expected and expected != actual:
                    errs.add(rel, f"front matter title != H1: {expected!r} vs {actual!r}")

            # Only check placeholder conventions on pilot files (with front matter)
            check_placeholders(body, rel, errs)
        else:
            # --- Legacy file (no front matter) ---
            # No placeholder check on legacy files to avoid false positives
            pass

    # --- 3. Resolve chains_to references ---
    for src, ref in all_chains_to:
        if ref not in all_ids and ref not in tombstones:
            errs.add(src, f"chains_to -> unresolved id {ref}")

    # --- 4. Validate pack manifests ---
    if PACKS_DIR.is_dir() and pack_schema is not None:
        pack_validator = Draft202012Validator(pack_schema)
        for path in sorted(PACKS_DIR.glob("*.pack.yaml")):
            rel = str(path.relative_to(ROOT))
            try:
                data = yaml.safe_load(path.read_text(encoding="utf-8"))
            except yaml.YAMLError as e:
                errs.add(rel, f"pack YAML error: {e}")
                continue
            if not isinstance(data, dict):
                errs.add(rel, "pack is not a mapping")
                continue

            for err in pack_validator.iter_errors(data):
                errs.add(rel, f"pack schema: {err.message}")

            # Step-level checks
            step_ids = [
                s.get("id")
                for s in data.get("steps", [])
                if isinstance(s, dict)
            ]
            seen_step_ids: set[str] = set()
            for sid in step_ids:
                if sid in seen_step_ids:
                    errs.add(rel, f"duplicate step id: {sid}")
                seen_step_ids.add(sid)

            for step in data.get("steps", []) or []:
                if not isinstance(step, dict):
                    continue
                pid = step.get("prompt_id")
                if isinstance(pid, str) and pid not in all_ids and pid not in tombstones:
                    errs.add(
                        rel,
                        f"step {step.get('id')}: prompt_id {pid} not found in library",
                    )
                out_s = step.get("output_schema")
                if isinstance(out_s, str) and not (ROOT / out_s).is_file():
                    errs.add(
                        rel,
                        f"step {step.get('id')}: output_schema not found: {out_s}",
                    )
                for inp in step.get("inputs_from", []) or []:
                    if isinstance(inp, dict):
                        ref_step = inp.get("step")
                        if ref_step not in seen_step_ids:
                            errs.add(
                                rel,
                                f"step {step.get('id')}: inputs_from references unknown step {ref_step}",
                            )

            # DAG acyclic check
            graph: dict[str, list[str]] = {
                sid: [] for sid in step_ids if sid
            }
            for step in data.get("steps", []) or []:
                if not isinstance(step, dict):
                    continue
                dest = step.get("id")
                for inp in step.get("inputs_from", []) or []:
                    if isinstance(inp, dict):
                        src = inp.get("step")
                        if src in graph and dest in graph:
                            graph[src].append(dest)
            if _has_cycle(graph):
                errs.add(rel, "pack DAG contains a cycle")

            entry = data.get("entry_step")
            if entry and entry not in seen_step_ids:
                errs.add(rel, f"entry_step {entry} not found among steps")
            for term in data.get("terminal_steps", []) or []:
                if term not in seen_step_ids:
                    errs.add(rel, f"terminal_step {term} not found among steps")

    # --- 5. Validate golden test fixtures ---
    golden_dir = ROOT / "tests" / "golden"
    if golden_dir.is_dir():
        for expected in sorted(golden_dir.glob("*.expected.json")):
            rel = str(expected.relative_to(ROOT))
            try:
                data = json.loads(expected.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errs.add(rel, f"invalid JSON: {e}")
                continue

            schema_hint = data.get("$schema_ref") if isinstance(data, dict) else None
            if isinstance(schema_hint, str):
                target = ROOT / schema_hint
                if not target.is_file():
                    errs.add(rel, f"$schema_ref not found: {schema_hint}")
                    continue
                try:
                    schema = json.loads(target.read_text(encoding="utf-8"))
                except json.JSONDecodeError as e:
                    errs.add(rel, f"referenced schema invalid: {e}")
                    continue
                payload = {k: v for k, v in data.items() if k != "$schema_ref"}
                for err in Draft202012Validator(schema).iter_errors(payload):
                    errs.add(rel, f"golden fails schema: {err.message}")
            else:
                errs.add(rel, "missing $schema_ref key in golden expected JSON")

    # --- Report ---
    if errs.ok():
        prompt_count = len(walk_prompt_files())
        print(f"OK \u2014 {len(all_ids)} canonical IDs, {prompt_count} files scanned.")
        return 0
    else:
        errs.report()
        print(f"\n{len(errs.errors)} error(s)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
