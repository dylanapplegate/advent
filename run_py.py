import os
import sys
import platform
import subprocess
import importlib.util

from watchdog.events import FileSystemEventHandler


def clear_console():
    # Detect the operating system
    system = platform.system()

    if system == "Windows":
        # Use 'cls' for Windows command prompt/PowerShell
        os.system("cls")
    else:
        # Use 'clear' for Linux, macOS, and other Unix-like systems
        os.system("clear")


def run_tests_and_solution(year, day):
    day_padded = f"day{day.zfill(2)}"
    solution_path = os.path.join(year, day_padded, "python")

    if not os.path.exists(solution_path):
        print(f"Error: Solution path not found at {solution_path}")
        return

    # Run tests
    env = os.environ.copy()
    env["PYTHONPATH"] = solution_path + os.pathsep + env.get("PYTHONPATH", "")
    test_result = subprocess.run(
        ["pytest", "-k", solution_path], capture_output=True, text=True, env=env
    )

    print(test_result.stdout)
    print(test_result.stderr)

    if test_result.returncode != 0:
        print("Tests Failed. Skipping final solution run.")
        return

    print("All tests passed!")

    # Run solution
    input_file_path = os.path.join(year, day_padded, "input.txt")
    with open(input_file_path, "r") as f:
        input_data = f.read()

    spec = importlib.util.spec_from_file_location(
        f"{year}.{day_padded}.python.solution",
        os.path.join(solution_path, "solution.py"),
    )
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)

    part1_result = solution_module.part1(input_data)
    part2_result = solution_module.part2(input_data)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, year, day):
        self.year = year
        self.day = day

    def on_modified(self, event):
        if event.src_path.endswith("solution.py"):
            clear_console()
            print("Solution file changed. Re-running tests...")
            run_tests_and_solution(self.year, self.day)


def main():
    if len(sys.argv) != 3:
        print("Usage: python run_py.py <YEAR> <DAY>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    run_tests_and_solution(year, day)


if __name__ == "__main__":
    main()
