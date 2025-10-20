import re
from collections import Counter


def get_part1_tuple(row):
    pattern = r"\d+"
    digit_strings = re.findall(pattern, row)
    return (int(digit_strings[0]), int(digit_strings[1]))


def part1(input_data):

    rows = [get_part1_tuple(row) for row in input_data.strip().split("\n")]
    left = sorted([values[0] for values in rows])
    right = sorted([values[1] for values in rows])
    zipped = [(lValue, rValue) for lValue, rValue in zip(left, right)]
    diffs = [abs(lValue - rValue) for lValue, rValue in zipped]
    return sum(diffs)


def part2(input_data):

    rows = [get_part1_tuple(row) for row in input_data.strip().split("\n")]
    left = [values[0] for values in rows]
    right = Counter([values[1] for values in rows])
    values = [num * right[num] for num in left]
    print(values)
    return sum(values)
