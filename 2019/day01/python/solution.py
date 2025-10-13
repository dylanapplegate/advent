import math
from typing import Union


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

def calculate_recursive_fuel(mass):
    fuel = calculate_fuel(mass)
    if fuel <= 0:
        return 0
    return fuel + calculate_recursive_fuel(fuel)

def part1(input_data: Union[str, int]):
    if isinstance(input_data, str) and "\n" in input_data:
        masses = [int(line.strip()) for line in input_data.split("\n")]
    elif isinstance(input_data, str):
        masses = [int(input_data.strip())]
    else:
        masses = [input_data]

    total_fuel = sum(calculate_fuel(mass) for mass in masses)
    return str(total_fuel)


def part2(input_data):
    if isinstance(input_data, str) and "\n" in input_data:
        masses = [int(line.strip()) for line in input_data.split("\n")]
    elif isinstance(input_data, str):
        masses = [int(input_data.strip())]
    else:
        masses = [input_data]

    total_fuel = sum(calculate_recursive_fuel(mass) for mass in masses)
    return str(total_fuel)