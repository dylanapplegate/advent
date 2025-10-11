from collections import Counter
from itertools import accumulate, takewhile


def part1(input_data):
    counted = Counter(input_data)
    return str(counted["("] - counted[")"])


def part2(input_data):
    moves = (1 if char == "(" else -1 for char in input_data)

    cumulative_floors = accumulate(moves)


    safe_floors = list(takewhile(lambda f: f >= 0, cumulative_floors))

    return str(len(safe_floors)+1)
