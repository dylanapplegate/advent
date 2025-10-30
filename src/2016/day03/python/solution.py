def format_data(data: str) -> list[tuple[int, int, int]]:
    lines = [map(int, line.split()) for line in data.strip().splitlines()]
    number_lines = [
        (int(side1), int(side2), int(side3)) for side1, side2, side3 in lines
    ]
    return number_lines


def part1(input: str) -> int:
    return len(
        [
            True
            for side1, side2, side3 in format_data(input)
            if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1
        ]
    )


def part2(input: str) -> int:
    matrix = format_data(input)
    valid_triangles: int = 0

    for c in range(0, 3):
        for r in range(0, len(matrix), 3):
            side1 = matrix[r + 0][c]
            side2 = matrix[r + 1][c]
            side3 = matrix[r + 2][c]

            is_valid = (
                side1 + side2 > side3
                and side1 + side3 > side2
                and side2 + side3 > side1
            )

            valid_triangles += 1 if is_valid else 0

    return valid_triangles
