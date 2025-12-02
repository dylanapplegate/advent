def format_input(input: str) -> list[tuple[str, str]]:
    return [
        (id_range.split("-")[0], id_range.split("-")[1])
        for id_range in input.split(",")
        if id_range
    ]


def get_invalid_single_repeat_ids(lower_bound: int, upper_bound: int) -> list[int]:
    invalid_ids = [
        id
        for id in range(lower_bound, upper_bound + 1)
        if not is_valid_single_repeat(str(id))
    ]
    return invalid_ids


def get_invalid_multi_repeat_ids(lower_bound: int, upper_bound: int) -> list[int]:
    invalid_ids = [
        id
        for id in range(lower_bound, upper_bound + 1)
        if not is_valid_multi_repeats(str(id))
    ]
    return invalid_ids


def is_valid_single_repeat(id: str) -> bool:
    mid = len(id) // 2
    return id[0:mid] != id[mid:]


def is_valid_multi_repeats(id: str) -> bool:
    return id not in (id * 2)[1:-1]


def part1(input: str) -> int:
    ranges = format_input(input)
    return sum(
        invalid_ids
        for lower, upper in ranges
        for invalid_ids in get_invalid_single_repeat_ids(int(lower), int(upper))
    )


def part2(input: str) -> int:
    ranges = format_input(input)
    invalid_ids = [
        invalid_ids
        for lower, upper in ranges
        for invalid_ids in get_invalid_multi_repeat_ids(int(lower), int(upper))
    ]
    return sum(invalid_ids)
