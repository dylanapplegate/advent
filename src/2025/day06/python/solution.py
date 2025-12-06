import math
import re

ROW = tuple[str, ...]
ROWS = list[ROW]


def parse_grid_simple(input: str) -> ROWS:
    return [
        tuple(cols) for line in input.splitlines() if line for cols in [line.split()]
    ]


def parse_grid_fixed_width(input: str) -> ROWS:
    lines = [line for line in input.splitlines() if line]
    sign_row = lines[-1]

    pattern = r"[\*\+]\s*"

    col_spans = [m.span() for m in re.finditer(pattern, sign_row)]

    formatted_rows = []
    for line in lines[:-1]:
        row_segments = tuple(line[start:end] for start, end in col_spans)
        formatted_rows.append(row_segments)

    formatted_rows.append(tuple(sign_row.split()))

    return formatted_rows


def calculate(nums: list[int], sign: str) -> int:
    if sign == "*":
        return math.prod(nums)
    return sum(nums)


def decode_vertical_num(column_segments: tuple[str, ...]) -> int:
    segments = column_segments[:-1]
    right_to_left_nums = []

    max_len = max(len(s) for s in segments)

    for offset in range(1, max_len + 1):
        chars = [
            s[-offset] for s in segments if len(s) >= offset and s[-offset].strip()
        ]

        string_num = "".join(chars).strip()

        if string_num:
            right_to_left_nums.append(int(string_num))

    return calculate(right_to_left_nums, column_segments[-1])


def solve_problem_by_col2(rows: ROWS, col: int) -> int:
    sign = rows[-1][col]
    nums = [row[col] for row in rows[0:-1]]
    right_to_left_nums: list[int] = list()
    max_len = max(len(num) for num in nums)

    for offset in range(1, max_len + 1):
        string_num_list = [num[-1 * offset] for num in nums if num[-1 * offset].strip()]
        string_num = "".join(string_num_list).strip()
        if string_num:
            num = int(string_num)
            right_to_left_nums.append(num)

    return calculate(right_to_left_nums, sign)


def part1(puzzle_input: str) -> int:
    rows = parse_grid_simple(puzzle_input)

    total = 0

    for col in zip(*rows):
        sign = col[-1]
        nums = [int(n) for n in col[:-1]]
        total += calculate(nums, sign)

    return total


def part2(input: str) -> int:
    rows = parse_grid_fixed_width(input)

    return sum(decode_vertical_num(col) for col in zip(*rows))
