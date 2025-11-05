from functools import reduce
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




def part2(input):
    pass