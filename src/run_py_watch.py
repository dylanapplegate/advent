import os
import sys
import subprocess
import importlib.util
import time
import platform
from typing import Any, Optional

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def clear_console() -> None:
    # Detect the operating system
    system = platform.system()

    if system == "Windows":
        # Use 'cls' for Windows command prompt/PowerShell
        os.system("cls")
    else:
        # Use 'clear' for Linux, macOS, and other Unix-like systems
        os.system("clear")


def run_tests_and_solution(year: str, day: str) -> None:
    day_padded = f"day{day.zfill(2)}"
    solution_path = os.path.join("src", year, day_padded, "python")

    if not os.path.exists(solution_path):
        print(f"Error: Solution path not found at {solution_path}")
        return

    # Run tests
    env = os.environ.copy()
    env["PYTHONPATH"] = solution_path + os.pathsep + env.get("PYTHONPATH", "")
    test_result = subprocess.run(
        [
            "./.venv/bin/pytest",
            "src/test_solutions.py",
            "-k",
            f"test_solution and {year}/{day_padded}",
        ],
        capture_output=True,
        text=True,
        env=env,
    )

    print(test_result.stdout)
    print(test_result.stderr)

    if test_result.returncode != 0:
        print("Tests Failed. Skipping final solution run.")
        return

    print("All tests passed!")

    # Remove the module from sys.modules to ensure changes are picked up
    module_name = f"{year}.{day_padded}.python.solution"
    if module_name in sys.modules:
        del sys.modules[module_name]

    # Run solution
    input_file_path = os.path.join("src", year, day_padded, "input.txt")
    with open(input_file_path, "r") as f:
        input_data = f.read()

    spec = importlib.util.spec_from_file_location(
        f"{year}.{day_padded}.python.solution",
        os.path.join(solution_path, "solution.py"),
    )
    if spec is None or spec.loader is None:
        print(f"Error: Could not load solution module for {year}/{day_padded}")
        return
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)

    part1_result: Optional[str] = None
    part2_result: Optional[str] = None

    if hasattr(solution_module, "part1"):
        part1_result = solution_module.part1(input_data)
    if hasattr(solution_module, "part2"):
        part2_result = solution_module.part2(input_data)

    print(f"Part 1: {part1_result}")
    print(f"Part 2: {part2_result}")


class ChangeHandler(FileSystemEventHandler):
    def __init__(self, year: str, day: str) -> None:
        self.year = year
        self.day = day

    def on_modified(self, event: Any) -> None:
        if event.src_path.endswith("solution.py"):
            clear_console()
            print("Solution file changed. Re-running tests...")
            try:
                run_tests_and_solution(self.year, self.day)
            except Exception as e:
                print(f"Error during re-run: {e}")


def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python run_py.py <YEAR> <DAY>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]

    run_tests_and_solution(year, day)

    day_padded = f"day{day.zfill(2)}"
    solution_path = os.path.join("src", year, day_padded, "python")
    event_handler = ChangeHandler(year, day)
    observer = Observer()
    observer.schedule(event_handler, solution_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
