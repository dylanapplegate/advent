from collections import defaultdict
from functools import reduce
import re


def format_input(input: str) -> list[str]:
    return [line for line in input.strip().splitlines() if line.strip()]


def check_if_valid(y: int, start: int, end: int, schematic: list[str]) -> bool:
    ROW_START = max(0, y - 1)
    ROW_END = min(len(schematic) - 1, y + 1)
    COL_START = max(0, start - 1)
    COL_END = min(len(schematic[0]) - 1, end + 1)

    pattern = r"[^\d\.]"

    for y in range(ROW_START, ROW_END + 1):
        search_string = schematic[y][COL_START : COL_END + 1]
        search_result = re.search(pattern, search_string)
        if search_result is not None:
            return True

    return False


def get_gear_for_number(
    y: int, start: int, end: int, schematic: list[str]
) -> list[tuple[int, int]]:  # return (y, x)
    ROW_START = max(0, y - 1)
    ROW_END = min(len(schematic) - 1, y + 1)
    COL_START = max(0, start - 1)
    COL_END = min(len(schematic[0]) - 1, end + 1)

    gears: list[tuple[int, int]] = list()

    gear_pattern = re.compile(r"\*")

    for y in range(ROW_START, ROW_END + 1):
        search_result = gear_pattern.search(
            schematic[y], pos=COL_START, endpos=COL_END + 1
        )
        if search_result:
            start = search_result.start()
            gears.append((y, start))

    return gears


def part1(input: str) -> int:
    schematic = format_input(input)
    digit_pattern = re.compile(r"\d+")
    schematic_sum = 0

    for y, line in enumerate(schematic):
        search_index = 0

        while match := digit_pattern.search(line, pos=search_index):
            start, end = match.span()
            number_string = match.group(0)
            search_index = end

            if check_if_valid(y, start, end - 1, schematic):
                schematic_sum += int(number_string)

    return schematic_sum


def part2(input: str) -> int:
    schematic = format_input(input)
    digit_pattern = re.compile(r"\d+")
    gears: dict[tuple[int, int], list[int]] = defaultdict(list)

    for y, line in enumerate(schematic):
        search_index = 0

        while match := digit_pattern.search(line, pos=search_index):
            start, end = match.span()
            search_index = end
            number = int(match.group(0))

            number_gears = get_gear_for_number(y, start, end - 1, schematic)

            for gear in number_gears:
                gears[gear].append(number)

    return sum(
        reduce(lambda acc, num: acc * num, nums, 1)
        for nums in gears.values()
        if len(nums) == 2
    )
