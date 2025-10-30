from typing import cast


def format_data(data: str) -> list[tuple[int, int, int]]:
    lines = [
        cast(tuple[int, int, int], tuple(map(int, line.split())))
        for line in data.strip().splitlines()
        if len(line.split()) == 3
    ]

    return lines


def is_valid_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a


def part1(input: str) -> int:
    return sum(is_valid_triangle(a, b, c) for a, b, c in format_data(input))


def part2(input: str) -> int:
    matrix = format_data(input)
    valid_triangles: int = 0

    all_sides = [side for triangle in matrix for side in triangle]

    for c in range(0, 3):
        valid_triangles += sum(
            [
                is_valid_triangle(all_sides[i], all_sides[i + 3], all_sides[i + 6])
                for i in range(c, len(all_sides), 9)
            ]
        )

    return valid_triangles
