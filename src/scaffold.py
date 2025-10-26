import os
import sys


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python scaffold.py <YEAR> <DAY>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]
    day_padded = f"day{day.zfill(2)}"

    base_dir = os.path.join("src", year, day_padded)

    if os.path.exists(base_dir):
        print(
            f"Error: Directory '{base_dir}' already exists. "
            "Please delete it if you wish to rescaffold."
        )
        sys.exit(1)

    py_dir = os.path.join(base_dir, "python")
    ts_dir = os.path.join(base_dir, "typescript")

    # Create directories
    os.makedirs(py_dir)
    os.makedirs(ts_dir)

    # Create empty input.txt
    with open(os.path.join(base_dir, "input.txt"), "w") as f:
        pass

    # Create example_1.txt
    with open(os.path.join(base_dir, "example_1.txt"), "w") as f:
        f.write(
            """--- Part 1 ---
Input:

Output:

--- Part 2 ---
Input:

Output:
"""
        )

    # Create test_data.json
    with open(os.path.join(base_dir, "test_data.json"), "w") as f:
        f.write(
            """
{
  "part1": [],
  "part2": []
}
"""
        )

    # Python solution template
    py_solution_template = """

def part1(input):
    pass

def part2(input):
    pass
"""
    with open(os.path.join(py_dir, "solution.py"), "w") as f:
        f.write(py_solution_template.strip())

    # TS solution template
    ts_solution_template = """

export function part1(input: string): number | string | undefined {
  return undefined;
}

export function part2(input: string): number | string | undefined {
  return undefined;
}
"""
    with open(os.path.join(ts_dir, "solution.ts"), "w") as f:
        f.write(ts_solution_template.strip())

    print(f"Scaffolding for Year {year}, Day {day} created successfully.")


if __name__ == "__main__":
    main()
