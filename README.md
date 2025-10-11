# Advent of Code Solver

This project is a multi-language solver for Advent of Code puzzles, with support for Python and JavaScript.

## 🚀 Getting Started

1.  **Install Dependencies and Setup Environment:**
    ```bash
    pnpm
    ```

This single command will install all Node.js dependencies and then automatically create a Python virtual environment (`.venv`) and install all Python dependencies into it.

## Scaffolding

To create the directory structure for a new puzzle, use the `scaffold.py` script:

```bash
pnpm scaffold <YEAR> <DAY>
```

## Running Solutions

Solutions are run using root-level scripts that automatically validate examples first.

- **Python Execution:** `pnpm run:py <YEAR> <DAY>`
- **JavaScript Execution:** `pnpm run:js <YEAR> <DAY>`

**Workflow:** The runner will first execute all example tests (from `test_data.json` and `example_*.txt`). ONLY if all tests pass will it then load the `input.txt` file and print the final solution for Part 1 and Part 2.
