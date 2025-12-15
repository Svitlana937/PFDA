# Assignments

This folder contains course / practice assignments for the PFDA repository. Each assignment lives in its own subdirectory and should include a short README describing the task, the solution, and how to run tests or example usage.

Purpose
- Keep assignment tasks, solutions, and tests organized.
- Provide consistent structure so reviewers/instructors can run and grade easily.
- Make it straightforward for contributors to add new assignments.

Repository layout (convention)
- assignments/
  - assignment-01/
    - README.md        ← task description + run instructions for this assignment
    - solution.py      ← canonical solution (or solution.ipynb / solution.js / ...)
    - tests/           ← automated tests (pytest, unittest, jest, etc.)
    - data/            ← input files needed by the assignment (if any)
  - assignment-02/
  - README.md         ← this file

File / naming conventions
- Assignment directories should be named `assignment-XX` where `XX` is a zero-padded number (01, 02, ...).
- Solution files:
  - Python: `solution.py` (or `solution.ipynb` for notebooks)


How to run an assignment (examples)
- Python script
  - Create a virtual environment, install deps:
    - python3 -m venv .venv
    - source .venv/bin/activate
    - pip install -r requirements.txt
  - Run:
    - python assignment-01/solution.py
- Jupyter notebook
  - jupyter notebook assignment-01/solution.ipynb
- Pytest (from repository root)
  - pytest assignments/assignment-01/tests
- Node
  - npm install (if package.json present)
  - node assignments/assignment-02/solution.js
- Java
  - javac assignments/assignment-03/Solution.java
  - java -cp assignments/assignment-03 Solution

Dependencies
- Top-level `requirements.txt` can list common Python dependencies. If an assignment needs extra dependencies, include a local `requirements.txt` in that assignment folder and document installation in that assignment's README.
- For Node assignments, include `package.json` inside that assignment folder if needed.


Contribution workflow
1. Create a branch: `git checkout -b feature/assignment-XX`
2. Add your assignment in `assignments/assignment-XX/` following the conventions above.
3. Include tests and a `README.md` for that assignment describing the problem and how to run tests.
4. Commit with a meaningful message: `feat(assignment-03): add solution and tests`
5. Push and open a Pull Request targeting `main`. In the PR title include the assignment number: `Assignment 03 — <short title>`
6. Link any issue or task number in the PR description if applicable.

Commit message guideline
- Use a short prefix: `feat`, `fix`, `chore`, `docs`, `test`
- Example: `feat(assignment-04): implement binary search and tests`

Coding style
- Python: follow PEP8. Use docstrings for functions and modules.
- JavaScript: follow standard/ESLint rules if present.
- Provide inline comments for non-obvious logic and a short note at the top of the solution explaining the approach and complexity.


Contact / maintainers
- Repo owner / maintainer: @Svitlana937
- For questions about a specific assignment, open an issue and reference the assignment directory.

License
- Follow the repository LICENSE (see top-level LICENSE file) unless the assignment has a special license noted in its folder.

---
