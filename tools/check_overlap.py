#!/usr/bin/env python3
"""Detect verbatim overlap between library prompts and third-party source texts.

Why this exists
---------------
Prompts have thin-to-no copyright, so the library's legal exposure is not that
someone copies us — it is that we ship someone else's expression. A previous
version of this library adapted an "All rights reserved" publication and
re-licensed it under CC BY 4.0. That is the failure mode this guards against.

Copyright protects expression, not ideas. So the signal we care about is
*consecutive verbatim wording*, not topical similarity. Two prompts about PDPA
breach notification will share vocabulary; that is fine and unavoidable. A
68-word identical run is not.

Usage
-----
    python3 tools/check_overlap.py --blocklist ~/path/to/reference-texts

The blocklist directory holds plain-text copies of every third-party
publication ever consulted. It is deliberately NOT committed to this repo:
those files are other people's copyrighted work. Keep it outside the tree (or
gitignored) and share it with collaborators out of band.

Exit codes: 0 = clean, 1 = overlap above threshold, 2 = misuse.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

SHINGLE = 8
DEFAULT_MAX_RUN = 15

# Ordinary legal and prompt-engineering boilerplate. These are set phrases that
# any two documents in this field will share without one copying the other, so
# counting them produces false positives that train people to ignore the gate.
ALLOWED_PHRASES = [
    "where attachments are referenced restrict analysis",
    "think through this step by step",
    "do not reference any external sources",
    "personal data protection act",
    "rules of court 2021",
    "generative artificial intelligence",
]


def normalise(text: str) -> list[str]:
    """Lowercase, drop punctuation and markdown, return a word list."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)  # fenced code
    text = re.sub(r"[*_`#>|\[\]()]", " ", text)  # markdown furniture
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return text.split()


def shingles(words: list[str], n: int = SHINGLE) -> set[tuple[str, ...]]:
    return {tuple(words[i : i + n]) for i in range(len(words) - n + 1)}


def longest_verbatim_run(words: list[str], source: set[tuple[str, ...]]) -> tuple[int, str]:
    """Length and text of the longest consecutive run also present in source."""
    best_len, best_at = 0, 0
    run_start = None
    for i in range(len(words) - SHINGLE + 1):
        if tuple(words[i : i + SHINGLE]) in source:
            if run_start is None:
                run_start = i
            length = i + SHINGLE - run_start
            if length > best_len:
                best_len, best_at = length, run_start
        else:
            run_start = None
    if not best_len:
        return 0, ""
    return best_len, " ".join(words[best_at : best_at + best_len])


def is_allowed(passage: str) -> bool:
    return any(p in passage for p in ALLOWED_PHRASES)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--blocklist", required=True, help="dir of third-party .txt files")
    ap.add_argument("--root", default=".", help="library root to scan")
    ap.add_argument("--max-run", type=int, default=DEFAULT_MAX_RUN)
    args = ap.parse_args()

    block_dir = pathlib.Path(args.blocklist).expanduser()
    if not block_dir.is_dir():
        print(f"error: blocklist dir not found: {block_dir}", file=sys.stderr)
        return 2

    source_shingles: set[tuple[str, ...]] = set()
    sources = sorted(block_dir.glob("*.txt"))
    for f in sources:
        source_shingles |= shingles(normalise(f.read_text(errors="ignore")))
    if not source_shingles:
        print(f"error: no .txt files in {block_dir}", file=sys.stderr)
        return 2

    print(f"Blocklist: {len(sources)} source(s), {len(source_shingles):,} unique {SHINGLE}-grams")
    for f in sources:
        print(f"  - {f.name}")
    print()

    root = pathlib.Path(args.root)
    targets = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)

    failures, flagged = [], []
    for path in targets:
        words = normalise(path.read_text(errors="ignore"))
        if len(words) < SHINGLE:
            continue
        own = shingles(words)
        hits = own & source_shingles
        if not hits:
            continue
        pct = 100.0 * len(hits) / len(own)
        run_len, passage = longest_verbatim_run(words, source_shingles)
        rel = path.relative_to(root)
        if run_len > args.max_run and not is_allowed(passage):
            failures.append((rel, pct, run_len, passage))
        else:
            flagged.append((rel, pct, run_len))

    if flagged:
        print("Below threshold (shared boilerplate — informational):")
        for rel, pct, run_len in flagged:
            print(f"  {pct:5.2f}%  longest run {run_len:3d}w  {rel}")
        print()

    if failures:
        print(f"FAIL — {len(failures)} file(s) exceed {args.max_run} consecutive verbatim words:\n")
        for rel, pct, run_len, passage in failures:
            print(f"  {rel}")
            print(f"    overlap {pct:.2f}%, longest run {run_len} words")
            print(f'    "{passage[:220]}…"\n')
        return 1

    print(f"PASS — {len(targets)} files scanned, no verbatim run over {args.max_run} words.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
