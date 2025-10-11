
import os
import sys
import subprocess
import importlib.util

def main():
    if len(sys.argv) != 3:
        print("Usage: python run_py.py <YEAR> <DAY>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]
    day_padded = f"day{day.zfill(2)}"
    solution_path = os.path.join(year, day_padded, "python")

    if not os.path.exists(solution_path):
        print(f"Error: Solution path not found at {solution_path}")
        sys.exit(1)

    # Run tests
    test_result = subprocess.run(["pytest", solution_path], capture_output=True, text=True)

    if test_result.returncode != 0:
        print("Tests Failed. Skipping final solution run.")
        print(test_result.stdout)
        print(test_result.stderr)
        sys.exit(1)
    
    print("All tests passed!")

    # Run solution
    input_file_path = os.path.join(year, day_padded, "input.txt")
    with open(input_file_path, "r") as f:
        input_data = f.read()

    spec = importlib.util.spec_from_file_location(
        f"{year}.{day_padded}.python.solution", 
        os.path.join(solution_path, "solution.py")
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)

    part1_result = solution_module.part1(input_data)
    part2_result = solution_module.part2(input_data)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")

if __name__ == "__main__":
    main()
