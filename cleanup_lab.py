"""Remove instructor tooling from a prepared assignment copy."""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
PHASES = (
    "01_initialization", "02_planning", "03_execution",
    "04_testing", "05_shipping",
)
TOOLING = ("AGENTS.md", "TEMPLATE_SETUP.md", "setup_lab.py", "cleanup_lab.py")
PLACEHOLDER = re.compile(r"\{\{[A-Z][A-Z0-9_]*\}\}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview without changing files.")
    args = parser.parse_args()
    readme = ROOT / "README.md"
    required = [readme, *(ROOT / phase for phase in PHASES)]
    if not readme.is_file() or any(not path.is_dir() for path in required[1:]):
        parser.error("Run this script from a complete lab template copy with all five phase folders.")
    if any(path.is_symlink() or not path.resolve().is_relative_to(ROOT) for path in required):
        parser.error("Student materials must be inside this repository.")

    original = readme.read_bytes().decode("utf-8")
    cleaned = re.sub(r"^> \*\*Instructor setup:\*\*[^\r\n]*\r?\n(?:\r?\n)?", "", original, flags=re.MULTILINE)
    unfinished = []
    student_files = [readme]
    for phase in PHASES:
        student_files.extend(path for path in (ROOT / phase).rglob("*") if path.is_file())
    for path in student_files:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            parser.error(f"Student file points outside the repository: {path}")
        try:
            content = cleaned if path == readme else path.read_bytes().decode("utf-8")
        except UnicodeDecodeError:
            continue
        if "\x00" not in content and PLACEHOLDER.search(content):
            unfinished.append(str(path.relative_to(ROOT)))
    if unfinished:
        parser.error("Fill in remaining placeholders before cleanup: " + ", ".join(unfinished))

    targets = [ROOT / name for name in TOOLING if (ROOT / name).exists()]
    cache = ROOT / "__pycache__"
    # Remove only bytecode produced by the instructor scripts.
    if cache.is_dir():
        targets.extend(path for path in cache.iterdir()
                       if path.name.startswith(("setup_lab.", "cleanup_lab.")) and path.suffix == ".pyc")
    for path in targets:
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT) or not path.is_file():
            parser.error(f"Refusing to remove an unexpected path: {path}")

    print(f"Assignment: {ROOT}")
    if cleaned != original:
        print("Remove instructor setup note from README.md")
    for path in targets:
        print(f"Remove {path.relative_to(ROOT)}")
    print("Keep README.md, all phase folders and contents, .git, and .gitignore.")
    if args.dry_run:
        print("Preview only. No files changed.")
        return

    if cleaned != original:
        readme.write_bytes(cleaned.encode("utf-8"))
    for path in targets:
        path.unlink()
    if cache.is_dir() and not any(cache.iterdir()):
        cache.rmdir()
    print("Cleanup complete. Review, commit, and push your student assignment.")


if __name__ == "__main__":
    main()
