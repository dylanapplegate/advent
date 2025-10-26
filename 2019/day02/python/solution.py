def format_input(input: str) -> list[int]:
    return [int(num) for num in input.strip().split(",") if num]


def part1(input: str, bypass_sub: bool = False) -> int:
    program = format_input(input)

    if program[1] != 9 and not bypass_sub:  # do not change the example provided
        program[1] = 12
        program[2] = 2

    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break

        input1_index = program[i + 1]
        input2_index = program[i + 2]
        insertion_index = program[i + 3]

        if opcode == 1:
            program[insertion_index] = program[input1_index] + program[input2_index]
        elif opcode == 2:
            program[insertion_index] = program[input1_index] * program[input2_index]

    return program[0]


def part2(input):
    desired_outcome = 19690720

    for x in range(0, 100):
        for y in range(0, 100):
            program = format_input(input)
            program[1] = x
            program[2] = y

            if desired_outcome == part1(",".join(map(str, program)), True):
                return 100 * x + y
