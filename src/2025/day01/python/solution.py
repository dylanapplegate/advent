def format_input(input: str) -> list[tuple[str, int]]:
    rotations = [(str(line[:1]), int(line[1:])) for line in input.splitlines() if line]
    return rotations


def part1(input: str) -> int:
    rotations = format_input(input)
    value = 50
    zero_count = 0

    for direction, distance in rotations:
        if direction == "R":
            value = (value + distance) % 100
        else:
            value = (value + (100 - (distance % 100))) % 100

        if value == 0:
            zero_count += 1

    return zero_count


def part2(input: str) -> int:
    rotations = format_input(input)
    value = 50
    zero_count = 0

    for direction, distance in rotations:
        additive = 0

        if direction == "L":
            additive = -1
        else:
            additive = 1

        counter = distance

        while counter > 0:
            value += additive

            if value == -1:
                value = 99
            elif value == 100:
                value = 0

            if value == 0:
                zero_count += 1

            counter -= 1

    return zero_count
