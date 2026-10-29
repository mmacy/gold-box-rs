#!/usr/bin/env python3
"""Block commits and pushes that would add game data to the repository.

The original Gold Box games are copyrighted, so no file from a game, from a
GOG installer, or recorded from the original game may enter the history of
this public repository. The Git hooks in `.githooks/` and the `game-data`
workflow run this script, and it rejects any file that:

- has the same SHA-256 hash as a file listed in
  `tools/game-data/known-files.sha256`,
- has a name or an extension that the games, their installers, disk images,
  archives, or disassemblers use,
- is binary, unless `tools/game-data/allowed-binaries.txt` lists it, or
- is larger than 1 MB, unless `tools/game-data/allowed-binaries.txt` lists it.

Usage:

    python3 tools/check_game_data.py staged
    python3 tools/check_game_data.py commits origin/main..HEAD
    python3 tools/check_game_data.py commits --all
    python3 tools/check_game_data.py hash ~/games/pools-of-darkness
"""

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWN_FILES = ROOT / "tools" / "game-data" / "known-files.sha256"
ALLOWED_BINARIES = ROOT / "tools" / "game-data" / "allowed-binaries.txt"
MAX_BYTES = 1_000_000

# Extensions of the games' files (DAX archives, the overlay, drivers, saves,
# configuration, and the PDF manuals), of installers, disk images, and
# archives, and of disassembly and decompiler output.
BLOCKED_EXTENSIONS = frozenset("""
    dax ovr exe com drv bat cfg acf bma sms sav sfx dat glb tlb chr pal fnt
    pdf voc xmi
    pkg dmg msi bin iso img ima cue mdf nrg
    zip 7z rar tar gz tgz xz bz2 lha lzh arj
    asm lst c h gzf gpr rep idb i64
""".split())

# Game files without an extension, DOSBox configurations from GOG, and GOG
# installer names.
BLOCKED_NAMES = re.compile(r"^(items|poolrad|save|dosbox.*\.conf|setup_.*|gog_.*)$", re.IGNORECASE)

ZERO_SHA = "0" * 40


def git(*args: str) -> bytes:
    """Run a Git command in the repository and return its output."""
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True).stdout


def read_hash_list(path: Path) -> dict[str, str]:
    """Read a file of `sha256  label` lines into a map from hash to label."""
    entries = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                digest, _, label = line.partition(" ")
                entries[digest.lower()] = label.strip()
    return entries


def staged_blobs() -> list[tuple[str, str]]:
    """Return the `(blob, path)` pairs that the next commit adds or changes."""
    out = git("diff", "--cached", "--raw", "-z", "--no-renames", "--diff-filter=ACMR")
    return parse_raw(out)


def commit_blobs(rev_args: list[str]) -> list[tuple[str, str]]:
    """Return the `(blob, path)` pairs that the given commits add or change.

    Args:
        rev_args: Arguments for `git rev-list`, like `origin/main..HEAD` or
            `--all`.
    """
    pairs = []
    for commit in git("rev-list", *rev_args).decode().split():
        out = git("diff-tree", "-r", "-m", "-z", "--root", "--no-commit-id", "--raw",
                  "--no-renames", "--diff-filter=ACMR", commit)
        pairs.extend(parse_raw(out))
    return list(dict.fromkeys(pairs))


def parse_raw(out: bytes) -> list[tuple[str, str]]:
    """Parse `git diff --raw -z` output into `(blob, path)` pairs."""
    fields = out.split(b"\0")
    pairs = []
    for meta, path in zip(fields[0::2], fields[1::2]):
        parts = meta.decode().split()
        if len(parts) >= 4 and parts[3] != ZERO_SHA:
            pairs.append((parts[3], path.decode(errors="replace")))
    return pairs


def is_binary(data: bytes) -> bool:
    """Return True if the data has a NUL byte or isn't valid UTF-8."""
    if b"\0" in data[:8192]:
        return True
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return True
    return False


def problems_with(path: str, data: bytes, known: dict[str, str], allowed: dict[str, str]) -> list[str]:
    """Return the reasons a file may not be committed, or an empty list."""
    digest = hashlib.sha256(data).hexdigest()
    if digest in known:
        return [f"it's a copy of the original file {known[digest]}"]
    reasons = []
    name = Path(path).name
    suffix = Path(path).suffix.lower().lstrip(".")
    if suffix in BLOCKED_EXTENSIONS:
        reasons.append(f"files ending in .{suffix} aren't allowed")
    if BLOCKED_NAMES.match(name):
        reasons.append(f"files named {name} aren't allowed")
    if allowed.get(digest) != path:
        if is_binary(data):
            reasons.append("it's a binary file that tools/game-data/allowed-binaries.txt doesn't list")
        elif len(data) > MAX_BYTES:
            reasons.append("it's larger than 1 MB and tools/game-data/allowed-binaries.txt doesn't list it")
    return reasons


def check(pairs: list[tuple[str, str]]) -> int:
    """Check each blob and print what's wrong. Returns the exit status."""
    known = read_hash_list(KNOWN_FILES)
    allowed = read_hash_list(ALLOWED_BINARIES)
    failures = 0
    for blob, path in pairs:
        data = git("cat-file", "blob", blob)
        for reason in problems_with(path, data, known, allowed):
            print(f"{path}: {reason}", file=sys.stderr)
            failures += 1
    if failures:
        print("\nGame data and copyrighted files must stay out of this repository. "
              "To commit a binary file you made, like a diagram, ask the owner to add it "
              "to tools/game-data/allowed-binaries.txt.", file=sys.stderr)
        return 1
    return 0


def print_hashes(folders: list[str]) -> int:
    """Print a `sha256  label` line for every file in the folders."""
    for folder in folders:
        base = Path(folder).expanduser()
        for file in sorted(p for p in base.rglob("*") if p.is_file()):
            digest = hashlib.sha256(file.read_bytes()).hexdigest()
            print(f"{digest}  {base.parent.name}/{base.name}/{file.relative_to(base)}")
    return 0


def main() -> int:
    # argparse rejects a leading option like --all, so the arguments after
    # `commits` go to git rev-list as they are.
    if sys.argv[1:2] == ["commits"]:
        return check(commit_blobs(sys.argv[2:] or ["HEAD"]))
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="mode", required=True)
    sub.add_parser("staged", help="check the files staged for the next commit")
    commits = sub.add_parser("commits", help="check every file the commits add or change")
    commits.add_argument("rev_args", nargs=argparse.REMAINDER, help="arguments for git rev-list")
    hashes = sub.add_parser("hash", help="print hash lines for known-files.sha256")
    hashes.add_argument("folders", nargs="+")
    args = parser.parse_args()
    if args.mode == "staged":
        return check(staged_blobs())
    if args.mode == "commits":
        return check(commit_blobs(args.rev_args or ["HEAD"]))
    return print_hashes(args.folders)


if __name__ == "__main__":
    sys.exit(main())
