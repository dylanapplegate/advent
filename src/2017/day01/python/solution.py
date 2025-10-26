def part1(input_data: str) -> str:
    N = len(input_data)
    total_sum = sum(
        int(input_data[i])
        for i in range(N)
        if input_data[i] == input_data[((i + 1) % N)]
    )
    return str(total_sum)


def part2(input_data: str) -> str:
    N = len(input_data)
    offset = N // 2
    total_sum = sum(
        int(input_data[i])
        for i in range(N)
        if input_data[i] == input_data[((i + offset) % N)]
    )
    return str(total_sum)
