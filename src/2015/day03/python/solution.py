move_delta = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

# def format_data(input: str) -> list[str]:
#     return [line for line in input.strip().splitlines() if line.strip()]


def part1(moves: str) -> int:
    y, x = 0, 0
    visited = set()
    visited.add((y, x))
    for move in moves:
        dy, dx = move_delta[move]
        y, x = y + dy, x + dx
        visited.add((y, x))

    return len(visited)


def part2(moves: str) -> int:
    s_y, s_x, r_y, r_x = 0, 0, 0, 0
    visited = set()
    visited.add((0, 0))

    for i, move in enumerate(moves):
        if i % 2 == 1:
            y, x = s_y, s_x
        else:
            y, x = r_y, r_x

        dy, dx = move_delta[move]
        y, x = y + dy, x + dx
        visited.add((y, x))

        if i % 2 == 1:
            s_y, s_x = y, x
        else:
            r_y, r_x = y, x

    return len(visited)
