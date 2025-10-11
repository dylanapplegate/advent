## Final Project Specification for Advent of Code Solver

This specification defines the required file structure, technology stack, and workflow for a multi-language Advent of Code project.

### 1. Technology and Tooling Stack

| Feature | Python Stack | JavaScript Stack | Scaffolding |
| :---- | :---- | :---- | :---- |
| **Language** | Python 3.10+ | Node.js (LTS) | Python |
| **Package Manager** | pip (via requirements.txt) | npm (via package.json) | N/A |
| **Test Runner** | **pytest** | **jest** | N/A |
| **Code Quality** | **flake8**, **black**, **mypy** | **eslint**, **prettier** | N/A |
| **Solution Interface** | part1(input), part2(input) | part1(input), part2(input) | N/A |

### 2. File Structure

The project uses a **Year-centric** structure, keeping all resources for a given day in one place:

* /aoc-solver/
* ├── .gitignore
* ├── README.md
* ├── requirements.txt
* ├── package.json
* ├── **scaffold.py** # The dedicated setup script
* ├── **<YEAR>** (e.g., 2023)
* │   └── **<DAY_NN>** (e.g., day01, day25)
* │       ├── **python/**
* │       │   ├── solution.py
* │       │   └── test_solution.py
* │       ├── **javascript/**
* │       │   ├── solution.js
* │       │   └── solution.test.js
* │       ├── **input.txt** # Actual puzzle input (empty upon scaffold)
* │       ├── **example_1.txt** # Example input (for multi-line inputs)
* │       └── **test_data.json** # Example input (for short, inline examples)
* └── ...

### 3. Input and Testing Logic

Solutions must accept the raw file content as a string. The test runners must be capable of handling two different example input formats:

#### A. Structured JSON Examples (test_data.json)

This format is for multiple, small, single-line examples.

* The file must contain an object with part1 and part2 arrays, each holding objects with input and expected keys.
* **Testing Priority:** The test runners **must prioritize** loading and running tests from test_data.json if the file is present.

**Example test_data.json:**

```json
* {
*   "part1": [
*     { "input": "((", "expected": 2 },
*     { "input": "())", "expected": -1 }
*   ],
*   "part2": [
*     { "input": ")", "expected": 1 }
*   ]
* }
```

#### B. Separated Text Examples (example_*.txt)

This format is for larger, multi-line inputs where the input and expected outputs are separated by a delimiter.

* The input data occupies the lines above the --- separator.
* The expected answers follow the format Part 1: <answer> and Part 2: <answer> below the separator.

**Example example_1.txt:**

* 1abc2
* pqr3stu8vwx
* ---
* Part 1: 142
* Part 2: 281

### 4. Scaffolding Mechanism

The **scaffold.py** script must be written in Python to simplify the setup process.

**Usage:**

```bash
* python scaffold.py <YEAR> <DAY>
* # Example: python scaffold.py 2023 1
```

**Actions:**

1. Validate inputs and create the structure: <YEAR>/day<DD>.
2. Create the python and javascript subdirectories.
3. Create an empty **input.txt**.
4. Create **example_1.txt** with the basic template (input lines above ---, expected answers below).
5. Create **test_data.json** with an empty { "part1": [], "part2": [] } structure.
6. Populate all four template files (solution.py, test_solution.py, solution.js, solution.test.js) with appropriate boilerplates, including imports, and the defined function signatures (part1, part2).

### 5. Setup Files

* **.gitignore:** Standard file to exclude build artifacts and local configurations.
* **README.md:** High-level summary for human users with setup and usage instructions.

### 6. New Requirement: `GEMINI.md`

The root of the project directory (`/aoc-solver/`) must contain a file named **`GEMINI.md`**.

### 7. `GEMINI.md` Content

This file must clearly document the key aspects of the project. The coding agent should be instructed to copy and paste this file into the prompt when requesting work on a new day or feature.

The content should include (but not be limited to):

1.  **Project Goal:** Solving Advent of Code problems across multiple years and languages.
2.  **Directory Structure:** A simple diagram showing the `<YEAR>/<DAY_NN>/` structure, the `python/` and `javascript/` subfolders, and the location of input files.
3.  **Core Tooling:** Listing the required tools for each language (`pytest`, `jest`, `black`, `eslint`, etc.).
4.  **Solution Interface:** Explicitly stating that solutions must be implemented as separate, signature-consistent functions: `part1(input: str)` and `part2(input: str)`.
5.  **Test Data Formats:**
    * **Inline Examples (`test_data.json`):** Used for short, multiple examples, and *prioritized* by the test runners.
    * **Block Examples (`example_*.txt`):** Used for larger, multi-line inputs, delimited by `---`.
6.  **Key Commands:** The exact commands for scaffolding, testing, linting, and running the code.
