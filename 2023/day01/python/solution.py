def format_data(input_data):
    return [row.strip() for row in input_data.strip().split("\n")]


def get_input_number(input):
    stripped_input = "".join([num for num in input.strip() if num.isdigit()])
    return int(stripped_input[0] + stripped_input[-1])


def part1(input_data):
    numbers = [get_input_number(num) for num in format_data(input_data)]
    return str(sum(numbers))


def part2(input_data):
    pass
