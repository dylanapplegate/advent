import importlib.util
import json
import re
from pathlib import Path
from types import ModuleType


def load_solution_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location("solution", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot find module at {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_solution(solution_path: Path) -> None:
    solution_dir = solution_path.parent
    day_dir = solution_dir.parent
    test_data_path = day_dir / "test_data.json"
    example_data_path = day_dir / "example_1.txt"

    solution = load_solution_module(solution_path)

    if test_data_path.exists():
        with open(test_data_path) as f:
            test_data = json.load(f)

        for part in ["part1", "part2"]:
            if part in test_data:
                for case in test_data[part]:
                    input_data = case["input"]
                    expected = case["expected"]

                    if hasattr(solution, part):
                        actual = getattr(solution, part)(input_data)
                        assert actual == expected, f"Failed on input: {input_data}"

    if example_data_path.exists():
        with open(example_data_path) as f:
            content = f.read()

        part1_match = re.search(
            r"--- Part 1 ---\nInput:\n(.*?)\nOutput:\n(.*?)(?=\n--- Part 2 ---|$)",
            content,
            re.DOTALL,
        )
        part2_match = re.search(
            r"--- Part 2 ---\nInput:\n(.*?)\nOutput:\n(.*?)$", content, re.DOTALL
        )

        if part1_match:
            input_data = part1_match.group(1)
            expected_output = part1_match.group(2)
            if hasattr(solution, "part1") and input_data and expected_output:
                actual = solution.part1(input_data)
                assert str(actual) == expected_output, (
                    f"Part 1 failed on example input: {input_data}"
                )

        if part2_match:
            input_data = part2_match.group(1)
            expected_output = part2_match.group(2)
            if hasattr(solution, "part2") and input_data and expected_output:
                actual = solution.part2(input_data)
                assert str(actual) == expected_output, (
                    f"Part 2 failed on example input: {input_data}"
                )
