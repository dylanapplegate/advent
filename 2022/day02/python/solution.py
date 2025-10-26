shapes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

beats = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

scores = {"Rock": 1, "Paper": 2, "Scissors": 3}


def format_data(input: str) -> list[tuple[str, ...]]:
    return [
        tuple(line.strip().split(maxsplit=1))
        for line in input.strip().splitlines()
        if line.strip()
    ]


def score_round(round: tuple[str, str]) -> int:
    opponent, self = round
    score = scores[shapes[self]]
    if beats[shapes[self]] == shapes[opponent]:
        score += 6
    elif shapes[self] == shapes[opponent]:
        score += 3

    return score


def part1(input_data: str) -> int:
    scored_rounds = [score_round(round_tuple) for round_tuple in format_data(input_data)]  # type: ignore
    return sum(scored_rounds)


def part2(input_data):
    pass
