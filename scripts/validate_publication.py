#!/usr/bin/env python3
"""Fail-closed publication validator; no external dependencies."""
import argparse, hashlib, json, pathlib, re, sys

ID = re.compile(r"[a-z][a-z0-9-]{1,79}\Z")
SHA = re.compile(r"[a-f0-9]{64}\Z")
COMMIT = re.compile(r"[a-f0-9]{40}\Z")
LANG = re.compile(r"[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})*\Z")
FIELDS = {"chapter_id", "edition_id", "language", "original_language", "title", "source_commit", "path", "sha256", "rights_status", "evidence_status", "author_approved"}
EVIDENCE = {"supported", "bounded", "insufficient_evidence", "not_applicable"}

def check(v, pattern, label):
    if not isinstance(v, str) or not pattern.fullmatch(v):
        raise ValueError(f"invalid {label}")

def validate_chapter(d, root):
    if not isinstance(d, dict) or FIELDS - d.keys():
        raise ValueError("missing chapter fields")
    for k in ("chapter_id", "edition_id"):
        check(d[k], ID, k)
    for k in ("language", "original_language"):
        check(d[k], LANG, k)
    check(d["source_commit"], COMMIT, "source_commit")
    check(d["sha256"], SHA, "sha256")
    if not isinstance(d["title"], str) or not d["title"].strip():
        raise ValueError("empty title")
    if d["rights_status"] != "cleared" or d["author_approved"] is not True:
        raise ValueError("publication requires rights clearance and author approval")
    if d["evidence_status"] not in EVIDENCE:
        raise ValueError("invalid evidence status")
    if d["language"] != d["original_language"]:
        if not isinstance(d.get("translation_of"), str) or not d["translation_of"].strip():
            raise ValueError("missing translation provenance")
    elif d.get("translation_of") is not None:
        raise ValueError("original text must not claim translation_of")
    path = d["path"]
    if not isinstance(path, str) or "\\" in path or path.startswith("/") or ".." in pathlib.PurePosixPath(path).parts or not path.startswith("chapters/"):
        raise ValueError("unsafe chapter path")
    target = (root / path).resolve()
    if not target.is_relative_to(root) or not target.is_file():
        raise ValueError("missing or escaping chapter file")
    if hashlib.sha256(target.read_bytes()).hexdigest() != d["sha256"]:
        raise ValueError("digest mismatch")
    return tuple(d[k] for k in ("chapter_id", "edition_id", "language"))

def validate_release(d, known):
    if not isinstance(d, dict) or not {"release_id", "chapters", "author_approved", "rights_status"} <= d.keys():
        raise ValueError("missing release fields")
    check(d["release_id"], ID, "release_id")
    if d["author_approved"] is not True or d["rights_status"] != "cleared":
        raise ValueError("release not approved or cleared")
    if not isinstance(d["chapters"], list) or not d["chapters"]:
        raise ValueError("empty release")
    seen = set()
    for e in d["chapters"]:
        if not isinstance(e, dict) or set(e) != {"chapter_id", "edition_id", "language"}:
            raise ValueError("malformed chapter reference")
        key = tuple(e[k] for k in ("chapter_id", "edition_id", "language"))
        if key not in known or key in seen:
            raise ValueError("unknown or duplicate chapter reference")
        seen.add(key)

def run(root):
    known, releases = set(), set()
    for p in sorted((root / "chapters").rglob("*.chapter.json")):
        key = validate_chapter(json.loads(p.read_text()), root)
        if key in known:
            raise ValueError("duplicate chapter identity")
        known.add(key)
    for p in sorted((root / "releases").glob("*.release.json")):
        d = json.loads(p.read_text())
        validate_release(d, known)
        if d["release_id"] in releases:
            raise ValueError("duplicate release identity")
        releases.add(d["release_id"])
    print(f"VALID: {len(known)} chapters, {len(releases)} releases")

if __name__ == "__main__":
    try:
        ap = argparse.ArgumentParser()
        ap.add_argument("--root", type=pathlib.Path, default=pathlib.Path(__file__).resolve().parents[1])
        args = ap.parse_args()
        run(args.root.resolve())
    except (ValueError, OSError, json.JSONDecodeError) as e:
        print(f"INVALID: {e}", file=sys.stderr)
        sys.exit(1)
