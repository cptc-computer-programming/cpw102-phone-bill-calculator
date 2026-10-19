"""Fill in a copy of the lab template using terminal prompts."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
TOKEN = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
FIXED = {"COURSE_CODE": "CPW 102", "COURSE_SLUG": "cpw102"}
FIELDS = [
    ("LAB_TITLE", "Lab title", False),
    ("LAB_SLUG", "Lab slug (lowercase words separated by hyphens)", False),
    ("LEARNING_GOALS", "Concepts and skills students will practice", True),
    ("SCENARIO", "Who needs the program, their problem, and desired result", True),
    ("EXPECTED_BEHAVIOR", "Inputs, processing rules, and output expectations", True),
    ("EXAMPLE_RUN", "Example terminal interaction with correct results", True),
    ("TECHNICAL_EXPECTATIONS", "Required features, organization, and conventions", True),
    ("ASSUMPTIONS_AND_LIMITS", "Input assumptions, validation, and allowed/excluded features", True),
    ("CASE_1_INPUTS", "Concrete inputs for a typical test case", True),
    ("CASE_2_FOCUS", "Behavior or boundary for the second test case", False),
    ("CASE_2_INPUTS", "Concrete inputs for the second test case", True),
]
SKIP_DIRS = {".git", ".venv", "venv", "env", "__pycache__", "node_modules"}


def template_files(root):
    """Read UTF-8 text files containing placeholders, excluding tooling."""
    found = []
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if (not path.is_file() or path.is_symlink()
                or any(part in SKIP_DIRS for part in relative.parts)
                or path.name == Path(__file__).name):
            continue
        raw = path.read_bytes()
        if b"\x00" in raw:
            continue
        try:
            content = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if TOKEN.search(content):
            found.append((path, content))
    return found


def ask(name, label, multiline):
    while True:
        print(f"\n{label}" + (" (multiline)" if multiline else ""))
        if multiline:
            lines = []
            while True:
                line = input()
                if not lines and not line.strip():
                    return None
                if line == "END":
                    break
                lines.append(line)
            value = "\n".join(lines).strip("\n")
        else:
            value = input("> ").strip()
        if not value.strip():
            return None
        elif TOKEN.search(value):
            print("Enter the actual lab details instead of a placeholder.")
        elif name == "LAB_SLUG" and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
            print("Use lowercase letters or numbers, with single hyphens between words.")
        else:
            return value


def main():
    files = template_files(ROOT)
    pending = {match.group(1) for _, content in files for match in TOKEN.finditer(content)}
    if not pending:
        print("No unfilled placeholders found. Use a fresh template copy for another lab.")
        return

    print(f"Lab setup: {ROOT}")
    print("Course: CPW 102 (cpw102)")
    print("This updates the files in this repository. Run it in your new assignment copy.")
    print("Press Ctrl+C to cancel before saving. All answers are collected first.")
    print("Press Enter without typing an answer to leave its placeholder for later.")
    print("For multiline fields, type END on its own line to finish; blank lines after your first line are allowed.")
    values = dict(FIXED)
    try:
        for name, label, multiline in FIELDS:
            if name in pending:
                values[name] = ask(name, label, multiline)
        # Include any additional placeholders added to future labs.
        for name in sorted(pending - values.keys()):
            values[name] = ask(name, name.replace("_", " ").capitalize(), True)
    except (KeyboardInterrupt, EOFError):
        print("\nSetup canceled. No files changed.")
        return

    for path, content in files:
        newline = "\r\n" if "\r\n" in content else "\n"
        updated = TOKEN.sub(
            lambda match: (values[match.group(1)].replace("\n", newline)
                           if values[match.group(1)] is not None else match.group(0)),
            content,
        )
        if updated != content:
            path.write_bytes(updated.encode("utf-8"))
            print(f"Updated {path.relative_to(ROOT)}")
    print("\nSetup complete. Review the files and finish the Template Setup checklist.")
    skipped = [name for name, value in values.items() if value is None]
    if skipped:
        print("Placeholders left unchanged: " + ", ".join(skipped))


if __name__ == "__main__":
    main()
