from typing import Dict, List, Optional


WORD_TO_NUMBER_MAP: Dict[str, str] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def format_data(input_data: str) -> List[str]:
    return [row.strip() for row in input_data.strip().split("\n")]


def get_input_number(input_str: str) -> int:
    stripped_input = "".join([num for num in input_str.strip() if num.isdigit()])
    return int(stripped_input[0] + stripped_input[-1])


def part1(input_data: str) -> str:
    numbers = [get_input_number(num) for num in format_data(input_data)]
    return str(sum(numbers))


def map_string(input_data: str) -> int:
    first_index: float = float("inf")
    first_match: Optional[str] = None
    last_index: float = float("-inf")
    last_match: Optional[str] = None

    for term in WORD_TO_NUMBER_MAP:
        first_term_index = input_data.find(term)
        if first_term_index != -1 and first_term_index < first_index:
            first_index = float(first_term_index)
            first_match = term

        last_term_index = input_data.rfind(term)
        if last_term_index != -1 and last_term_index > last_index:
            last_index = float(last_term_index)
            last_match = term

    if first_match is not None:
        first_match_mapped = WORD_TO_NUMBER_MAP[first_match]
    else:
        first_match_mapped = "0"

    if last_match is not None:
        last_match_mapped = WORD_TO_NUMBER_MAP[last_match]
    else:
        last_match_mapped = "0"

    return int(first_match_mapped + last_match_mapped)


def part2(input_data: str) -> int:
    mapped_coordinates = [map_string(row) for row in input_data.strip().split("\n")]
    return sum(mapped_coordinates)
