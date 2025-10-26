def format_input(input: str):
    return [int(line.strip()) for line in input.strip().split("\n")]


def part1(input_data):
    input_data = format_input(input_data)
    greater_than = sum(
        [1 for prev, current in zip(input_data, input_data[1:]) if current > prev]
    )
    return str(greater_than)


def part2(input_data):
    input_data = format_input(input_data)
    greater_than = sum(
        [1 for prev, current in zip(input_data, input_data[3:]) if current > prev]
    )
    return str(greater_than)
