
import sys
import os
import json
import pytest
from pathlib import Path
import importlib.util

def load_solution_module(path):
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_solution(solution_path):
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
                    if part == "part2":
                        if "expected_first_twice" in case:
                            expected = case["expected_first_twice"]
                        else:
                            continue
                    else:
                        expected = case["expected"]
                    
                    if hasattr(solution, part):
                        actual = getattr(solution, part)(input_data)
                        assert actual == expected, f"Failed on input: {input_data}"

    if example_data_path.exists():
        with open(example_data_path) as f:
            example_data = f.read()
        
        if "---" in example_data:
            input_data, expected_data = example_data.split("---", 1)
            input_data = input_data.strip()
            
            for line in expected_data.strip().split("\n"):
                if "Part 1" in line and hasattr(solution, "part1"):
                    expected_part1 = line.split(":")[1].strip()
                    if expected_part1:
                        actual = solution.part1(input_data)
                        assert actual == expected_part1, f"Part 1 failed on example input: {input_data}"
                
                if "Part 2" in line and hasattr(solution, "part2"):
                    expected_part2 = line.split(":")[1].strip()
                    if expected_part2:
                        actual = solution.part2(input_data)
                        assert actual == expected_part2, f"Part 2 failed on example input: {input_data}"
