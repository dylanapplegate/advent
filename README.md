# Advent of Code Solver

This project is a multi-language solver for Advent of Code puzzles, with support for Python and JavaScript.

## Setup

### Python

1.  Create a virtual environment: `python -m venv .venv`
2.  Activate it: `source .venv/bin/activate`
3.  Install dependencies: `pip install -r requirements.txt`

### JavaScript

1.  Install dependencies: `npm install`

## Scaffolding

To create the directory structure for a new puzzle, use the `scaffold.py` script:

```bash
python scaffold.py <YEAR> <DAY>
```

## Running Solutions

Solutions are run using root-level scripts that automatically validate examples first.

- **Python Execution:** `npm run run:py -- <YEAR> <DAY>`
- **JavaScript Execution:** `npm run run:js -- <YEAR> <DAY>`

**Workflow:** The runner will first execute all example tests (from `test_data.json` and `example_*.txt`). ONLY if all tests pass will it then load the `input.txt` file and print the final solution for Part 1 and Part 2.
