# Lab authoring instructions

This repository is an instructor template for CPW 102 Python labs. Course code is `CPW 102`; repository course slug is `cpw102`.

## Writing style

Prioritize brevity and clarity over exhaustive explanation in assignment materials and responses to the instructor. Use plain language, short paragraphs, and direct instructions. State each requirement once. Include examples or explanations only when they clarify something students need to do. Avoid filler, repeated reminders, and unnecessary background. Preserve essential requirements and constraints; concise writing must still be complete and unambiguous.

When asked to import an old assignment:

- Read the entire supplied assignment and the existing template before editing.
- Preserve its learning objectives, requirements, difficulty, restrictions, and provided starter code. Do not introduce new required features or solve the assignment.
- Organize the assignment into the five existing phase folders. Put the scenario, learning goals, expected behavior, examples, technical expectations, and assumptions in the problem statement.
- Adapt the planning and test worksheets to the assignment. Leave student requirements, design answers, pseudocode, expected test results, and run evidence blank. Preserve instructor-provided test inputs and examples.
- Keep the execution starter empty unless the original assignment supplies starter code or the instructor requests it. Keep solutions out of the student materials.
- Edit files directly; using the interactive setup script is optional. Replace known placeholders consistently. Leave unresolved details visible and report missing or conflicting requirements instead of inventing them.
- Keep the current GitHub Desktop, development-branch, pull-request, and Canvas workflow unless the instructor requests a change. Flag conflicting submission instructions in the old assignment.
- Verify example calculations, links, filenames, commands, and remaining placeholders. Report any decisions needed from the instructor.

Instructor tooling is `AGENTS.md`, `TEMPLATE_SETUP.md`, `setup_lab.py`, and `cleanup_lab.py`. When asked to prepare the assignment for students, use `python cleanup_lab.py --dry-run` to inspect the cleanup and then `python cleanup_lab.py` to perform it. Cleanup removes these files, including itself, and the README instructor note. Preserve the README, phase folders and contents, `.git`, and `.gitignore`. Do not run cleanup in the reusable template unless explicitly requested.
