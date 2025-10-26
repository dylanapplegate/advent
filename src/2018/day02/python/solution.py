from collections import Counter


def format_input(input: str) -> list[str]:
    return [line.strip() for line in input.strip().splitlines() if line]


def count_line(line: str) -> tuple[int, int]:  # (3Count, 2Count)
    counter = Counter(line)
    counts = (0, 0)
    if 3 in counter.values():
        counts = (1, counts[1])
    if 2 in counter.values():
        counts = (counts[0], 1)

    return counts


def part1(input: str) -> int:
    ids = format_input(input)
    counted_ids = [count_line(id) for id in ids]
    count3, count2 = zip(*counted_ids)

    return sum(count3) * sum(count2)


def get_duplicate(ids: list[str]) -> str:
    seen = set()

    for id in ids:
        if id in seen:
            return id

        seen.add(id)

    return ""


def part2(input):
    ids = format_input(input)

    for replace_index in range(len(ids[0])):
        subbed_ids = [id[0:replace_index] + id[replace_index + 1 :] for id in ids]
        duplicate = get_duplicate(subbed_ids)
        if duplicate:
            return duplicate

    return ""
