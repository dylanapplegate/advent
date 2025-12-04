Grid = list[list[str]]


def format_input(input: str) -> Grid:
    return [list(line) for line in input.splitlines() if line]


def has_max_rolls(grid: Grid, r: int, c: int, max_rolls: int) -> bool:
    if grid[r][c] != "@":
        return False

    roll_count = 0
    ROWS = len(grid)
    COLS = len(grid[0])

    for y in range(r - 1, r + 2):
        for x in range(c - 1, c + 2):
            if y < 0 or x < 0 or y >= ROWS or x >= COLS:
                continue
            if y == r and x == c or grid[y][x] != "@":
                continue

            # print(y, x, r, c, grid[y][x])
            roll_count += 1

            if roll_count > max_rolls:
                return False

    return True


def part1(input: str) -> int:
    grid = format_input(input)
    ROWS = len(grid)

    return sum(
        1
        for r in range(0, ROWS)
        for c in range(0, len(grid[r]))
        if has_max_rolls(grid, r, c, 3)
    )

    return 0


def part2(input: str) -> int:
    grid = format_input(input)
    ROWS = len(grid)

    roll_count = 0
    can_remove = True

    while can_remove:
        can_remove = False

        for r in range(0, ROWS):
            for c in range(0, len(grid[r])):
                if has_max_rolls(grid, r, c, 3):
                    can_remove = True
                    roll_count += 1
                    grid[r][c] = "."

    return roll_count
