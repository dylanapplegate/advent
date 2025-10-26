from typing import List, Tuple, Set, Optional


def part1(input_data: str) -> int:
    directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x, y = 0, 0
    direction = 0

    moves = input_data.split(", ")

    for move in moves:
        if move[0] == "R":
            direction = (direction + 1) % 4
        elif move[0] == "L":
            direction = (direction - 1 + 4) % 4

        distance = int(move[1:])
        dx, dy = directions[direction]

        x += dx * distance
        y += dy * distance

    return abs(x) + abs(y)


def part2(input_data: str) -> Optional[int]:
    directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    x, y = 0, 0
    direction = 0

    moves = input_data.split(", ")

    seen: Set[Tuple[int, int]] = {(x, y)}

    for move in moves:
        if move[0] == "R":
            direction = (direction + 1) % 4
        elif move[0] == "L":
            direction = (direction - 1 + 4) % 4

        distance = int(move[1:])
        dx, dy = directions[direction]

        for _ in range(distance):
            x += dx
            y += dy

            if (x, y) in seen:
                return abs(x) + abs(y)
            seen.add((x, y))

    return None
