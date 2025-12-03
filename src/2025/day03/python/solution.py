def format_input(input: str) -> list[str]:
    return [bank for bank in input.splitlines() if bank]


def get_max_joltage_2(bank: str) -> int:
    batteries = list(map(lambda k: int(k), list(bank)))
    left = batteries[0]
    right = batteries[1]

    for i in range(2, len(batteries)):
        current_max = left * 10 + right
        battery = batteries[i]

        if right * 10 + battery > current_max:
            left = right
            right = battery
        elif left * 10 + battery > current_max:
            right = battery

    return left * 10 + right


def get_batteries_total(batteries: list[int]) -> int:
    batteries_str = map(lambda b: str(b), batteries)
    return int("".join(batteries_str))


def get_max_joltage_12(bank: str) -> int:
    batteries = list(map(lambda k: int(k), list(bank)))
    max_batteries_list = batteries[0:12]
    max_batteries = get_batteries_total(max_batteries_list)

    for i in range(12, len(batteries)):
        temp_batteries = max_batteries_list + [batteries[i]]

        for o in range(0, len(max_batteries_list)):
            check_batteries = temp_batteries[0:o] + temp_batteries[o + 1 :]

            check_total = get_batteries_total(check_batteries)

            if check_total > max_batteries:
                max_batteries_list = check_batteries
                max_batteries = check_total

    return max_batteries


def part1(input: str) -> int:
    banks = format_input(input)
    return sum(get_max_joltage_2(bank) for bank in banks)


def part2(input: str) -> int:
    banks = format_input(input)
    return sum(get_max_joltage_12(bank) for bank in banks)
