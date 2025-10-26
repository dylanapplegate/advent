from collections import Counter
from typing import List, Tuple, Set


def format_input(input_str: str) -> List[str]:
    return [line.strip() for line in input_str.strip().splitlines() if line]


def count_line(line: str) -> Tuple[int, int]:  # (3Count, 2Count)
    counter = Counter(line)
    counts = (0, 0)
    if 3 in counter.values():
        counts = (1, counts[1])
    if 2 in counter.values():
        counts = (counts[0], 1)

    return counts


def part1(input_str: str) -> int:
    ids = format_input(input_str)
    counted_ids = [count_line(id) for id in ids]
    count3, count2 = zip(*counted_ids)

    return sum(count3) * sum(count2)


def get_duplicate(ids: List[str]) -> str:
    seen: Set[str] = set()

    for id_str in ids:
        if id_str in seen:
            return id_str

        seen.add(id_str)

    return ""


def part2(input_str: str) -> str:
    ids = format_input(input_str)

    for replace_index in range(len(ids[0])):
        subbed_ids = [id_str[0:replace_index] + id_str[replace_index + 1 :] for id_str in ids]
        duplicate = get_duplicate(subbed_ids)
        if duplicate:
            return duplicate

    return ""