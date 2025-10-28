## Advent of Code Project Spec

This project solves Advent of Code problems in Python and JavaScript.

### Core Concepts

*   **Structure:** Year-centric (`<YEAR>/<DAY_NN>`), with `python/` and `javascript/` subfolders.
*   **Solution Interface:** Implement `part1(input: str)` and `part2(input: str)` functions.
*   **Input:** Solutions receive raw file content as a string.

### Technology

| Feature         | Python                          | JavaScript               |
| :-------------- | :------------------------------ | :----------------------- |
| **Language**    | Python 3.10+                    | Node.js (LTS)            |
| **Package Mgr** | pip (`src/requirements.txt`)    | pnpm (`package.json`)    |
| **Test Runner** | `pytest`                        | `jest`                   |
| **Code Quality**| `flake8`, `black`, `mypy`       | `eslint`, `prettier`     |

### Testing

Test runners prioritize `test_data.json` over `example_*.txt` files.

*   **`test_data.json`**: For multiple, small, single-line examples.
    *   JSON format: `{ "part1": [{ "input": "...", "expected": "..." }], "part2": [...] }`
*   **`example_*.txt`**: For larger, multi-line inputs.
    *   Format: Input data, then `---`, then `Part 1: <answer>` and `Part 2: <answer>`.

### Workflow & Commands

1.  **Setup:** `pnpm install` (installs all JS and Python dependencies).
2.  **Scaffold:** `pnpm scaffold <YEAR> <DAY>`
3.  **Run Solution:**
    *   `pnpm run:py <YEAR> <DAY>`
    *   `pnpm run:js <YEAR> <DAY>`
    *   `pnpm run:py:watch <YEAR> <DAY>`
    *   `pnpm run:js:watch <YEAR> <DAY>`
    *   Runners execute tests first. Solution runs only if tests pass.
4.  **Test:** `pnpm test`
5.  **Validate Agent Work:**
    *   Run `pnpm test`.
    *   Run `pnpm run:js 2015 1` and `pnpm run:py 2015 1`.
    *   Update `GEMINI.md` with any relevant details.

### Shell Safety

*   All shell commands must be wrapped with a `timeout 30s` to prevent hangs.
    *   Example: `timeout 30s <command_to_run>`