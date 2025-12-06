import math
import re

ROW = tuple[str, ...]
ROWS = list[ROW]


def format_input(input: str) -> ROWS:
    return [
        tuple(cols) for line in input.splitlines() if line for cols in [line.split()]
    ]


def format_input2(input: str) -> ROWS:
    rows = [row for row in input.splitlines() if row]
    sign_row = rows[-1]
    pattern = r"[\*\+]\s*"

    matches = [
        (match.start(), match.end()) for match in list(re.finditer(pattern, sign_row))
    ]

    formatted_rows = [
        tuple(split_row)
        for row in rows[0:-1]
        for split_row in [[row[start:end] for start, end in matches]]
    ]

    formatted_rows.append(tuple(sign_row.split()))

    return formatted_rows


def handle_math(nums: list[int], sign: str) -> int:
    if sign == "*":
        return math.prod(nums)
    else:
        return sum(nums)


def solve_problem_by_col(rows: ROWS, col: int) -> int:
    sign = rows[-1][col]
    nums = [int(row[col]) for row in rows[0:-1]]
    return handle_math(nums, sign)


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

    return handle_math(right_to_left_nums, sign)


def part1(input: str) -> int:
    rows = format_input(input)
    return sum(solve_problem_by_col(rows, col) for col in range(len(rows[0])))


def part2(input: str) -> int:
    rows = format_input2(input)

    return sum(solve_problem_by_col2(rows, col) for col in range(len(rows[0])))
