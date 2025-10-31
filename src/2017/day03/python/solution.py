def format_data(input: str) -> list[tuple[int, ...]]:
    lines = [tuple(map(int, line.split())) for line in input.strip().splitlines()]
    return lines


def part1(input: str) -> int:
    return sum(max(nums) - min(nums) for nums in format_data(input))


def get_even_divisor(nums: tuple[int, ...]) -> int:
    sorted_nums = sorted(nums, reverse=True)

    generator = (
        a // b
        for a_index, a in enumerate(sorted_nums)
        for b in sorted_nums[a_index + 1 :]
        if a % b == 0
    )

    return next(generator, 0)


def part2(input: str) -> int:
    return sum(get_even_divisor(line) for line in format_data(input))
