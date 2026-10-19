# Template Setup

Use this repository as the starting point for a new Python lab. It follows the same five phases as the Freelance Quote Builder project.

Create a separate assignment repository from this template for each lab. Customize that repository before students create their own copies. Keep this repository generic so it can be reused.

## 1. Set the lab details

From your new assignment repository folder, run:

```text
python setup_lab.py
```

The program asks for the lab details below and replaces every occurrence of each answered placeholder in repository text files. Course code is always `CPW 102` and course slug is always `cpw102`; neither is prompted. Press Enter before typing an answer to leave that placeholder unchanged for editing later. For longer answers, paste multiple lines and type `END` on its own line when finished. Blank lines are allowed after the first line. All answers are collected before files are saved; press Ctrl+C to cancel before saving.

Run this in a fresh assignment copy for each lab. Rerunning a completed copy does not change its existing answers. The script skips itself, Git metadata, virtual environments, dependency folders, and binary files.

You can also fill in the placeholders manually. The names below appear inside double braces in the assignment files.

| Placeholder | What to enter |
| --- | --- |
| `LAB_TITLE` | Human-readable assignment title |
| `LAB_SLUG` | Short, lowercase assignment name with hyphens |
| `LEARNING_GOALS` | Concepts and skills students will practice |
| `SCENARIO` | Who needs the program, their problem, and the desired result |
| `EXPECTED_BEHAVIOR` | Inputs, processing rules, and output expectations |
| `EXAMPLE_RUN` | A representative terminal interaction with correct results |
| `TECHNICAL_EXPECTATIONS` | Required language features, code organization, and conventions |
| `ASSUMPTIONS_AND_LIMITS` | Valid input assumptions, validation expectations, and allowed or excluded features |
| `CASE_1_INPUTS` | Concrete inputs for a typical use case |
| `CASE_2_FOCUS` | A different behavior or boundary that students must test |
| `CASE_2_INPUTS` | Concrete inputs for that second case |

Student response areas are intentionally blank. Leave those for students to complete.

## 2. Prepare the assignment

- [ ] Update the title and repository naming pattern in [README](README.md).
- [ ] Write the [Problem Statement](01_initialization/01_problem_statement.md), including the learning goals. Describe the user's need clearly enough for students to derive requirements.
- [ ] Check that the example output agrees with the stated rules.
- [ ] Review [Product Requirements](02_planning/01_product_requirements.md) and [Engineering Design](02_planning/02_engineering_design.md). Adapt the prompts to the concepts taught in this lab.
- [ ] Keep [main.py](03_execution/main.py) empty, or add only the starter code students should receive. If you rename it, update the README and testing command.
- [ ] Supply concrete inputs in [Test Cases](04_testing/01_testing_cases.md). Add cases as needed to cover the requirements. Leave expected results and evidence for students.
- [ ] Review [Submission Instructions](05_shipping/01_submission_instructions.md). The default workflow uses GitHub Desktop, a `development` branch, an open pull request into `main`, and Canvas.
- [ ] Adjust repository visibility, group instructions, tools, and submission destination if your course uses different policies.

## 3. Check before distributing

- [ ] Confirm no `{{...}}` placeholders remain in student-facing files.
- [ ] Check links and file paths after any renaming.
- [ ] Confirm students can complete the lab using only the concepts and tools you allow.
- [ ] Verify the test inputs and example results against your own solution. Keep the solution out of the student starter repository.
- [ ] Run `python cleanup_lab.py --dry-run` to preview cleanup, then `python cleanup_lab.py` to remove the instructor tooling and README setup note.
- [ ] Commit and push the prepared assignment. Enable the assignment repository's template setting in GitHub if students will use **Use this template**.

The starter file intentionally has no implementation. Running it produces no output until students write their program.

## Cleanup for students

Run cleanup in the prepared assignment copy, before making it available to students. It checks for unfinished placeholders, then removes `AGENTS.md`, `TEMPLATE_SETUP.md`, `setup_lab.py`, and `cleanup_lab.py` itself. It also removes cached bytecode for the two scripts and the instructor setup note in the README.

The README, all five phase folders and their contents, `.git`, and `.gitignore` are preserved. Other files are left alone; review any extra files you added before publishing. Cleanup changes your local files only. Commit and push the removals afterward. Keep the setup tools in this reusable template repository.
