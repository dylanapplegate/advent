MOVE_DELTAS: dict[str, tuple[int, int]] = {
    "U": (1, 0),  # Up: +Y movement
    "D": (-1, 0), # Down: -Y movement
    "R": (0, 1),  # Right: +X movement
    "L": (0, -1)  # Left: -X movement
}

def format_wire(input: str) -> list[tuple[str, int]]:
    wire =  [
        (direction[0:1], int(direction[1:]))
        for direction in input.strip().split(",")
        if direction.strip()
    ]
    # print(format_wire)
    return wire



def format_data(input: str) -> tuple[list[tuple[str, int]], list[tuple[str, int]]]:
    wires = tuple(map(format_wire, input.strip().splitlines()))
    if len(wires) != 2:
        raise ValueError("there should only be two wires")

    return wires

def get_visited_set(directions: list[tuple[str, int]]) -> set[tuple[int, int]]:
    visited: set[tuple[int, int]] = set()
    y, x = 0, 0

    for direction, distance in directions:
        dy, dx = MOVE_DELTAS[direction]

        for _ in range(distance):
            y += dy
            x += dx

            visited.add((y, x))

    return visited

def get_steps_to_insection(directions: list[tuple[str, int]], intersections: set[tuple[int, int]]) -> dict[tuple[int, int], int]:
    steps_to_intersection: dict[tuple[int, int], int] = dict()
    y, x = 0, 0
    steps = 0

    for direction, distance in directions:
        dy, dx = MOVE_DELTAS[direction]

        for _ in range(distance):
            y += dy
            x += dx
            steps+=1

            coord = (y, x)

            if coord in intersections and coord not in steps_to_intersection:
                steps_to_intersection[coord] = steps


    return steps_to_intersection

def part1(input):
    wires = format_data(input)
    visited1 = get_visited_set(wires[0])
    visited2 = get_visited_set(wires[1])
    intersections = visited1.intersection(visited2)

    return min(abs(y) + abs(x) for y, x in intersections)



def part2(input):
    wires = format_data(input)
    visited1 = get_visited_set(wires[0])
    visited2 = get_visited_set(wires[1])
    intersections = visited1.intersection(visited2)
    steps1 = get_steps_to_insection(wires[0], intersections)
    steps2 = get_steps_to_insection(wires[1], intersections)

    intersection_total_steps = [
        step_count1 + step_count2
        for intersection1, step_count1 in steps1.items()
        for intersection2, step_count2 in steps2.items()
        if intersection1 == intersection2
    ]

    return min(intersection_total_steps)
