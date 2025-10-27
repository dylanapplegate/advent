PAD = (("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9"))
COMPLEX_PAD = (
    ("x", "x", "1", "x", "x"),
    ("x", "2", "3", "4", "x"),
    ("5", "6", "7", "8", "9"),
    ("x", "A", "B", "C", "x"),
    ("x", "x", "D", "x", "x"),
)

DIRECTION_MAP = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}


def format_data(input: str) -> list[str]:
    return input.strip().splitlines()


def part1(input: str) -> str:
    instructions = format_data(input)
    y, x = 1, 1
    code = ""

    for instruction in instructions:
        for move in instruction:
            dy, dx = DIRECTION_MAP[move]
            y, x = y + dy, dx + x
            y, x = min(y, 2), min(x, 2)
            y, x = max(y, 0), max(x, 0)

        code = code + PAD[y][x]

    return code


def is_valid_complex_coordinate(y: int, x: int) -> bool:
    return 0 <= y < 5 and 0 <= x < 5 and COMPLEX_PAD[y][x] != "x"


def part2(input: str) -> str:
    instructions = format_data(input)
    y, x = 1, 1
    code = ""

    for instruction in instructions:
        for move in instruction:
            dy, dx = DIRECTION_MAP[move]
            ny, nx = y + dy, x + dx

            if is_valid_complex_coordinate(ny, nx):
                y, x = ny, nx

        code = code + COMPLEX_PAD[y][x]

    return code
