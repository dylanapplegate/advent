from collections import Counter
from typing import List, Tuple


def extract_data(line: str) -> Tuple[int, int, str, str]:
    policy, password = line.strip().split(":", 1)
    password = password.strip()
    count_range, letter = policy.strip().split(maxsplit=1)
    min_part, max_part = count_range.strip().split("-", 1)
    min_count = int(min_part)
    max_count = int(max_part)

    return (min_count, max_count, letter, password)


def format_data(input_str: str) -> List[Tuple[int, int, str, str]]:
    return [extract_data(line) for line in input_str.strip().splitlines()]


def is_valid(policy: Tuple[int, int, str, str]) -> bool:
    min_count, max_count, char, password = policy
    password_char_count = Counter(password)
    return min_count <= password_char_count[char] <= max_count


def is_valid2(policy: Tuple[int, int, str, str]) -> bool:
    position1, position2, char, password = policy
    position1_valid = password[position1 - 1] == char
    position2_valid = password[position2 - 1] == char
    return (position1_valid and not position2_valid) or (
        position2_valid and not position1_valid
    )


def part1(input_data: str) -> int:
    policies_and_passwords = format_data(input_data)
    valid_passwords = [line for line in policies_and_passwords if is_valid(line)]
    return len(valid_passwords)


def part2(input_data: str) -> int:
    policies_and_passwords = format_data(input_data)
    valid_passwords = [line for line in policies_and_passwords if is_valid2(line)]
    return len(valid_passwords)
