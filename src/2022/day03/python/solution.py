import re
from collections import Counter

Compartments = tuple[str, str]

def split_line(line: str) -> Compartments:
    mid = len(line) // 2

    return (line[0:mid], line[mid:])

def format_input1(input: str) -> list[Compartments]:
    return [
        split_line(line)
        for line in input.strip().splitlines()
        if line.strip()
    ]

def format_input2(input: str) -> list[str]:
    return [
        line for line in input.strip().splitlines()
        if line.strip()
    ]


def get_letter_priority() -> dict[str, int]:
    priorities: dict[str, int] = dict()
    lower_case_additive = ord("a")
    upper_case_additive = ord("A")

    for i in range(26):
        lower_case_letter = chr(lower_case_additive + i)
        upper_case_letter = chr(upper_case_additive + i)
        lower_case_priority = i + 1
        upper_case_priority = i + 27

        priorities[lower_case_letter] = lower_case_priority
        priorities[upper_case_letter] = upper_case_priority

    return priorities

def get_line_intersect_priorities(compartments: Compartments) -> int:
    front_counter = Counter(compartments[0])
    back_counter = Counter(compartments[1])
    intersections = front_counter & back_counter
    letter_priorities = get_letter_priority()
    return sum (
        letter_priorities[letter]
        for letter, count in intersections.items()
    )

def part1(input):
    backpacks = format_input1(input)
    priorities = [
        get_line_intersect_priorities(backpack)
        for backpack in backpacks
    ]
    return sum(priorities)

def part2(input):
    backpacks = format_input2(input)
    letter_priorities = get_letter_priority()

    priority_sum = 0
    for i in range(0, len(backpacks), 3):
        counter1 = Counter(backpacks[i])
        counter2 = Counter(backpacks[i+1])
        counter3 = Counter(backpacks[i+2])
        together = counter1 & counter2 & counter3
        badge_id = together.most_common(1)[0][0]
        priority_sum += letter_priorities[badge_id]

    return priority_sum