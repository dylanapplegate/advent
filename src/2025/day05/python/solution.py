IngredientsFreshRange = tuple[int, int]
IngredientsFreshRanges = list[IngredientsFreshRange]
AvailableIngredientId = int
AvailableIngredients = list[AvailableIngredientId]


def format_input(
    input: str,
) -> tuple[IngredientsFreshRanges, AvailableIngredients]:
    fresh_ranges_text, available_text = input.split("\n\n")
    fresh_ranges: IngredientsFreshRanges = list()

    fresh_ranges = [
        (int(min_id), int(max_id))
        for line in fresh_ranges_text.splitlines()
        if line
        for min_id, max_id in [line.split("-")]
    ]

    for line in fresh_ranges_text.splitlines():
        min_id, max_id = line.split("-")
        fresh_ranges.append((int(min_id), int(max_id)))

    available_ingredients = [
        int(available_id)
        for available_id in available_text.splitlines()
        if available_id
    ]

    return (fresh_ranges, available_ingredients)


def prepare_ranges(
    ranges: IngredientsFreshRanges,
) -> IngredientsFreshRanges:
    sorted_ranges = sorted(ranges, key=lambda item: item[0])
    merged_ranges: IngredientsFreshRanges = [sorted_ranges[0]]

    for current_start, current_end in sorted_ranges[1:]:
        last_merged_start, last_merged_end = merged_ranges[-1]

        if current_start <= last_merged_end:
            max_end = max(last_merged_end, current_end)
            merged_ranges[-1] = (last_merged_start, max_end)
        else:
            merged_ranges.append((current_start, current_end))

    return merged_ranges


def is_fresh_id(
    ranges: IngredientsFreshRanges, ingredient_id: AvailableIngredientId
) -> bool:
    low, high = 0, len(ranges) - 1

    while low <= high:
        mid = low + (high - low) // 2
        min_id, max_id = ranges[mid]

        if min_id <= ingredient_id <= max_id:
            return True
        if ingredient_id < min_id:
            high = mid - 1
        else:
            low = mid + 1

    return False


def part1(input: str) -> int:
    fresh_ranges, ingredient_ids = format_input(input)
    working_ranges = prepare_ranges(fresh_ranges)
    return sum(
        1
        for ingredient_id in ingredient_ids
        if is_fresh_id(working_ranges, ingredient_id)
    )


def part2(input: str) -> int:
    fresh_ranges = format_input(input)[0]
    working_ranges = prepare_ranges(fresh_ranges)

    return sum(upper - lower + 1 for lower, upper in working_ranges)
