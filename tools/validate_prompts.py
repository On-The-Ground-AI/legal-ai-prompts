#!/usr/bin/env python3
"""Validator for legal-ai-prompts repo.

Run with: python tools/validate_prompts.py
Exits non-zero on any error. Prints a diagnostic per error.
Warnings do not cause non-zero exit.

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
        self.warnings: list[str] = []

    def add(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def warn(self, where: str, msg: str) -> None:
        self.warnings.append(f"{where}: {msg}")

    def ok(self) -> bool:
        return not self.errors

    def report(self) -> None:
        for w in self.warnings:
            print(f"[WARN] {w}", file=sys.stderr)
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


def load_sidecar(md_path: Path) -> dict | None:
    """Try to load a .meta.yaml sidecar file for a given .md file."""
    sidecar = md_path.with_suffix(".meta.yaml")
    if not sidecar.exists():
        return None
    try:
        raw = sidecar.read_text(encoding="utf-8")
        return yaml.safe_load(raw) or {}
    except (yaml.YAMLError, OSError):
        return None


def check_placeholders(body: str, where: str, errs: ValidationErrors) -> None:
    """Enforce [UPPERCASE_PLACEHOLDER] convention in pilot files."""
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


def _get_h1_title(content: str) -> str | None:
    """Extract the first H1 heading from markdown content."""
    m = re.search(r"^\s*#\s+(.+)$", content, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


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

    sidecar_files_seen: set[str] = set()

    for path in walk_prompt_files():
        rel = str(path.relative_to(ROOT))
        try:
            raw = path.read_bytes()
        except OSError as e:
            errs.add(rel, f"read error: {e}")
            continue

        if raw.startswith(b"\xef\xbb\xbf"):
            errs.add(rel, "UTF-8 BOM not allowed")
            raw = raw[3:]

        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            errs.add(rel, f"not valid UTF-8: {e}")
            continue

        fm = None
        has_front_matter = False

        # Check for inline front matter first
        m = FRONT_MATTER_RE.match(content)
        if m:
            has_front_matter = True
            yaml_text = m.group(1)
            if "\t" in yaml_text:
                errs.add(rel, "tab character in front matter (use spaces)")
            try:
                fm = yaml.safe_load(yaml_text) or {}
            except yaml.YAMLError as e:
                errs.add(rel, f"front matter YAML error: {e}")
                fm = None
            body = content[m.end():]
        else:
            body = content

        # Check for sidecar .meta.yaml file
        sidecar = path.with_suffix(".meta.yaml")
        if sidecar.exists():
            sidecar_rel = str(sidecar.relative_to(ROOT))
            sidecar_files_seen.add(sidecar_rel)
            if fm is not None:
                errs.add(rel, "has both inline front matter AND sidecar .meta.yaml (pick one)")
            else:
                has_front_matter = True
                try:
                    sidecar_raw = sidecar.read_text(encoding="utf-8")
                    if "\t" in sidecar_raw:
                        errs.add(sidecar_rel, "tab character in sidecar (use spaces)")
                    fm = yaml.safe_load(sidecar_raw) or {}
                except yaml.YAMLError as e:
                    errs.add(sidecar_rel, f"sidecar YAML error: {e}")
                    fm = None
                except OSError as e:
                    errs.add(sidecar_rel, f"read error: {e}")
                    fm = None

        # Validate front matter (from either source)
        if fm is not None and fm_schema is not None:
            source_label = rel if m else str(sidecar.relative_to(ROOT)) if sidecar.exists() else rel
            validate_front_matter(fm_schema, fm, source_label, errs)

            pid = fm.get("id") if isinstance(fm, dict) else None
            if isinstance(pid, str):
                if pid in all_ids:
                    errs.add(source_label, f"duplicate id {pid} (also in {all_ids[pid]})")
                else:
                    all_ids[pid] = source_label

            if isinstance(fm, dict):
                for ref in fm.get("chains_to", []) or []:
                    all_chains_to.append((pid or rel, ref))

                out_s = fm.get("output_schema")
                if isinstance(out_s, str):
                    if not (ROOT / out_s).is_file():
                        errs.add(source_label, f"output_schema not found: {out_s}")

            # Title match: check sidecar title against markdown H1
            if isinstance(fm, dict):
                expected_title = fm.get("title", "").strip()
                actual_title = _get_h1_title(body if m else content)
                if expected_title and actual_title and expected_title != actual_title:
                    errs.add(
                        source_label,
                        f"front matter title != H1: {expected_title!r} vs {actual_title!r}",
                    )

        # Only check placeholder conventions on pilot files (with front matter)
        if has_front_matter:
            check_placeholders(body if m else content, rel, errs)

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
                # prompt_id resolution is a WARNING, not an error.
                # Per-prompt IDs are generated at runtime by the Legal Box
                # loader and may not appear in file-level front matter.
                pid = step.get("prompt_id")
                if isinstance(pid, str) and pid not in all_ids and pid not in tombstones:
                    errs.warn(
                        rel,
                        f"step {step.get('id')}: prompt_id {pid} not in front-matter index (will be resolved at runtime)",
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

    # --- 6. Check for orphaned sidecar files ---
    for volume_dir in sorted(ROOT.glob("volume-*/")):
        for sidecar in sorted(volume_dir.glob("*.meta.yaml")):
            sidecar_rel = str(sidecar.relative_to(ROOT))
            if sidecar_rel not in sidecar_files_seen:
                md_path = sidecar.with_suffix("").with_suffix(".md")
                if not md_path.exists():
                    errs.add(sidecar_rel, "orphaned sidecar: no matching .md file")

    # --- Report ---
    errs.report()
    if errs.ok():
        prompt_count = len(walk_prompt_files())
        warn_msg = f" ({len(errs.warnings)} warning(s))" if errs.warnings else ""
        print(f"OK \u2014 {len(all_ids)} canonical IDs, {prompt_count} files scanned.{warn_msg}")
        return 0
    else:
        print(f"\n{len(errs.errors)} error(s), {len(errs.warnings)} warning(s)", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
