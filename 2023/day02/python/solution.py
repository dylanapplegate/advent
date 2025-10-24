def get_cube_maxes(game):
    cube_count = {}
    turns = game.strip().split(":")[1].strip().split(";")
    game_id = int(game.strip().split(":")[0].strip().split(" ")[1])

    for turn in turns:
        cubes_string = [cube.strip().split(" ") for cube in turn.split(",")]
        for count, color in cubes_string:
            count = int(count)
            cube_count[color] = max(count, cube_count.get(color, 0))

    return game_id, cube_count


def format_data(input_data):
    game_rows = input_data.strip().split("\n")
    game_dictionaries = [get_cube_maxes(game) for game in game_rows]
    return game_dictionaries


def is_possible(cube_count):
    on_hand = {"red": 12, "green": 13, "blue": 14}

    for color, count in on_hand.items():
        if color in cube_count and count < cube_count[color]:
            return False
    return True


def part1(input_data):
    games = format_data(input_data)

    valid_games = sum([game_id for game_id, game in games if is_possible(game)])
    return valid_games


def power_of_cubes(cube_count):
    return cube_count["red"] * cube_count["blue"] * cube_count["green"]


def part2(input_data):
    games = format_data(input_data)
    power_of_games = [power_of_cubes(game) for game_id, game in games]

    return sum(power_of_games)
