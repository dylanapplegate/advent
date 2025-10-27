def format_input(input: str) -> list[list[int]]:
    return [[int(num) for num in line.split()] for line in input.strip().splitlines()]


def part1(input: str) -> int:
    rows = format_input(input)
    differences = [max(row) - min(row) for row in rows]
    return sum(differences)


def get_even_division(row: list[int]) -> int:
    for left_index in range(len(row)):
        for right_index in range(left_index + 1, len(row)):
            if row[left_index] % row[right_index] == 0:
                return int(row[left_index] / row[right_index])
            if row[right_index] % row[left_index] == 0:
                return int(row[right_index] / row[left_index])
    return 0


def part2(input: str) -> int:
    divisors = [get_even_division(row) for row in format_input(input)]
    return sum(divisors)
