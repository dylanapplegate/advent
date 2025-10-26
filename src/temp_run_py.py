import sys
import os
import importlib.util

# Add the project root to the path to allow importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

def load_solution_module(year, day):
    day_padded = f"day{day.zfill(2)}"
    solution_path = os.path.join(year, day_padded, "python", "solution.py")
    spec = importlib.util.spec_from_file_location("solution", solution_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
        return module
    
    
    if __name__ == "__main__":
    year = "2015"
    day = "01"
    solution = load_solution_module(year, day)

    input_file_path = os.path.join(year, f"day{day.zfill(2)}", "input.txt")
    with open(input_file_path, "r") as f:
        input_data = f.read()

    print(f"Part 1: {solution.part1(input_data)}")
    print(f"Part 2: {solution.part2(input_data)}")
