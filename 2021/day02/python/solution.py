def format_data(input: str) -> list[tuple[str, int]]:
    lines = [
        (parts[0], int(parts[1]))
        for line in input.strip().splitlines()
        if (parts := line.strip().split())
    ]

    return lines


def part1(input_data):
    depth, position = 0, 0
    commands = format_data(input_data)
    for direction, units in commands:
        if direction == "forward":
            position += units
        elif direction == "up":
            depth -= units
        else:
            depth += units
    return depth * position


def part2(input_data):
    aim, depth, position = 0, 0, 0
    commands = format_data(input_data)
    for direction, units in commands:
        if direction == "forward":
            position += units
            depth += units * aim
        elif direction == "up":
            aim -= units
        else:
            aim += units
    return depth * position
