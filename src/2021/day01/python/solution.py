from typing import List


def format_input(input_str: str) -> List[int]:
    return [int(line.strip()) for line in input_str.strip().split("\n")]


def part1(input_data: str) -> str:
    input_data_list = format_input(input_data)
    greater_than = sum(
        [
            1
            for prev, current in zip(input_data_list, input_data_list[1:])
            if current > prev
        ]
    )
    return str(greater_than)


def part2(input_data: str) -> str:
    input_data_list = format_input(input_data)
    greater_than = sum(
        [
            1
            for prev, current in zip(input_data_list, input_data_list[3:])
            if current > prev
        ]
    )
    return str(greater_than)
