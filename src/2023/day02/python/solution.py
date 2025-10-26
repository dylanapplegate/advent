from typing import Dict, List, Tuple


def get_cube_maxes(game: str) -> Tuple[int, Dict[str, int]]:
    cube_count: Dict[str, int] = {}
    parts = game.strip().split(":")
    turns = parts[1].strip().split(";")
    game_id = int(parts[0].strip().split(" ")[1])

    for turn in turns:
        cubes_string = [cube.strip().split(" ") for cube in turn.split(",")]
        for count_str, color in cubes_string:
            count = int(count_str)
            cube_count[color] = max(count, cube_count.get(color, 0))

    return game_id, cube_count


def format_data(input_data: str) -> List[Tuple[int, Dict[str, int]]]:
    game_rows = input_data.strip().split("\n")
    game_dictionaries = [get_cube_maxes(game) for game in game_rows]
    return game_dictionaries


def is_possible(cube_count: Dict[str, int]) -> bool:
    on_hand = {"red": 12, "green": 13, "blue": 14}

    for color, count in on_hand.items():
        if color in cube_count and count < cube_count[color]:
            return False
    return True


def part1(input_data: str) -> int:
    games = format_data(input_data)

    valid_games = sum([game_id for game_id, game in games if is_possible(game)])
    return valid_games


def power_of_cubes(cube_count: Dict[str, int]) -> int:
    return cube_count["red"] * cube_count["blue"] * cube_count["green"]


def part2(input_data: str) -> int:
    games = format_data(input_data)
    power_of_games = [power_of_cubes(game) for game_id, game in games]

    return sum(power_of_games)
