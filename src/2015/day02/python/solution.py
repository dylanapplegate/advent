import math


def format_input(input: str) -> list[list[int]]:
    dimensions = [
        [int(dim) for dim in line.split("x")] for line in input.strip().splitlines()
    ]
    return dimensions


def calculate_paper(dimensions: list[int]) -> int:

    sides = (
        dimensions[0] * dimensions[1],
        dimensions[1] * dimensions[2],
        dimensions[2] * dimensions[0],
    )
    min_side = min(sides)

    total_square_feet = sum(map(lambda x: x * 2, sides))
    return int(min_side + total_square_feet)


def calculate_ribbon(dimensions: list[int]) -> int:
    min_two = sorted(dimensions)[0:2]
    face_ribbon = sum(map(lambda d: d * 2, min_two))
    bow_ribbon = math.prod(dimensions)
    return face_ribbon + bow_ribbon


def part1(input: str) -> int:
    paper = sum([calculate_paper(dimensions) for dimensions in format_input(input)])
    return paper


def part2(input: str) -> int:
    paper = sum([calculate_ribbon(dimensions) for dimensions in format_input(input)])
    return paper
