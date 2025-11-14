import math
from typing import Generator


def format_list(input: str) -> list[tuple[str, ...]]:
    return [tuple(line) for line in input.strip().splitlines()]


def iterate_on_slope(
    dr: int, dc: int
) -> Generator[tuple[int, int]]:  # (current_r, current_c)
    common_divisor = math.gcd(dr, dc)

    if common_divisor == 0:
        return

    dr_unit = dr // common_divisor
    dc_unit = dc // common_divisor

    current_r, current_c = 0, 0

    yield (current_r, current_c)
    while True:
        current_r += dr_unit
        current_c += dc_unit
        yield (current_r, current_c)


def get_tree_count(area: list[tuple[str, ...]], rise: int, run: int) -> int:
    N_rows = len(area)
    N_cols = len(area[0])
    iterator = iterate_on_slope(rise, run)
    tree_count = 0

    while (coords := next(iterator, None)) is not None and coords[0] < N_rows:
        y, x = coords
        x %= N_cols

        if area[y][x] == "#":
            tree_count += 1

    return tree_count


def part1(input: str) -> int:
    area = format_list(input)
    return get_tree_count(area, 1, 3)


def part2(input: str) -> int:
    area = format_list(input)
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

    return math.prod(get_tree_count(area, rise, run) for rise, run in slopes)
