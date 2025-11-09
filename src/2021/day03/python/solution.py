from functools import reduce
import math
def format_data(input: str) -> list[tuple[int, ...]]:
    return [
        tuple(map(lambda b: int(b), list(line)))
        for line in input.strip().splitlines()
    ]

def part1(input):
    numbers = format_data(input)
    mid = len(numbers) // 2
    results_sum_tuple = tuple(sum(elements) for elements in zip(*numbers))
    most_bit = tuple(map(lambda v: "1" if v >= mid else "0", results_sum_tuple))
    least_bit = tuple(map(lambda v: "1" if v < mid else "0", results_sum_tuple))
    most_int = int("".join(most_bit), 2 )
    least_int = int("".join(least_bit), 2 )

    return most_int * least_int


def get_most_num(input: list[tuple[int,...]]) -> int:
    potentials = input
    current_index = 0


    while len(potentials) > 1:
        mid = math.ceil(len(potentials) / 2)
        index_sum = tuple(sum(elements) for elements in zip(*potentials))[current_index]
        find_value = 1 if index_sum >= mid else 0
        potentials = [
            potential for potential in potentials
            if potential[current_index] == find_value
        ]
        current_index += 1

    return int("".join(map(str, potentials[0])), 2)

def get_least_num(input: list[tuple[int,...]]) -> int:
    potentials = input
    current_index = 0


    while len(potentials) > 1:
        mid = math.ceil(len(potentials) / 2)
        index_sum = tuple(sum(elements) for elements in zip(*potentials))[current_index]
        find_value = 1 if index_sum < mid else 0
        potentials = [
            potential for potential in potentials
            if potential[current_index] == find_value
        ]
        current_index += 1

    num = int("".join(map(str, potentials[0])), 2)
    return num


def part2(input):
    numbers = format_data(input)
    oxygen_rating = get_most_num(numbers)
    co2_scrubber = get_least_num(numbers)
    print(oxygen_rating, co2_scrubber)
    return oxygen_rating * co2_scrubber