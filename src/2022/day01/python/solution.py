def total(input_data: str) -> int:
    return sum([int(num) for num in input_data.strip().split("\n")])


def part1(input_data: str) -> str:
    groups = [group.strip() for group in input_data.strip().split("\n\n")]

    sums = [total(group) for group in groups]

    return str(max(sums))


def part2(input_data: str) -> str:
    groups = [group.strip() for group in input_data.strip().split("\n\n")]

    sums = [total(group) for group in groups]

    sums = sorted(sums, reverse=True)[:3]

    return str(sum(sums))
