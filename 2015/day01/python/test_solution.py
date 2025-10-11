import json
import os
import solution

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), "..", filename)) as f:
        return f.read()

def test_part1_json():
    test_data = json.loads(read_file("test_data.json"))
    for case in test_data["part1"]:
        assert solution.part1(case["input"]) == case["expected"]

def test_part2_json():
    test_data = json.loads(read_file("test_data.json"))
    for case in test_data["part2"]:
        assert solution.part2(case["input"]) == case["expected"]

def test_part1_example():
    example_data = read_file("example_1.txt")
    if "---" in example_data:
        input_data, expected = example_data.split("---")
        expected_part1 = [line for line in expected.split("\n") if "Part 1" in line][0].split(":")[1].strip()
        if expected_part1:
            assert str(solution.part1(input_data.strip())) == expected_part1

def test_part2_example():
    example_data = read_file("example_1.txt")
    if "---" in example_data:
        input_data, expected = example_data.split("---")
        expected_part2 = [line for line in expected.split("\n") if "Part 2" in line][0].split(":")[1].strip()
        if expected_part2:
            assert str(solution.part2(input_data.strip())) == expected_part2