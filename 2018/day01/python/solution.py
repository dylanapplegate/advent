def _parse_input(input_data):
    if not isinstance(input_data, list):
        input_data = input_data.split('\n')
    return [int(v.strip()) for v in input_data]

def part1(input_data):
    moves = _parse_input(input_data)
    return sum(moves)


def part2(input_data):
    moves = _parse_input(input_data)
    total = 0
    seen = {0}

    while True:
        for move in moves:
            total += move
            if total in seen:
                return total
            seen.add(total)
