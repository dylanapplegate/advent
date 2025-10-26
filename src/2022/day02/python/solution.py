shapes = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
beats = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
loses = {"Rock": "Paper", "Scissors": "Rock", "Paper": "Scissors"}
scores = {"Rock": 1, "Paper": 2, "Scissors": 3}


def format_data(input: str) -> list[tuple[str, str]]:
    return [
        (parts[0], parts[1])
        for line in input.strip().splitlines()
        for parts in [line.strip().split(maxsplit=1)]
        if line.strip()
    ]


def score_round(round: tuple[str, str]) -> int:
    opponent, me = round
    score = scores[shapes[me]]
    if beats[shapes[me]] == shapes[opponent]:
        score += 6
    elif shapes[me] == shapes[opponent]:
        score += 3

    return score


def score_round2(round: tuple[str, str]) -> int:
    shape, result = round
    mapped_shape = shapes[shape]
    score = 0
    if result == "X":  # Loss
        score += scores[beats[mapped_shape]]
    elif result == "Y":  # Draw
        score += 3 + scores[mapped_shape]
    else:  # wins
        score += 6 + scores[loses[mapped_shape]]

    return score


def part1(input_data: str) -> int:
    scored_rounds = [
        score_round(round_tuple) for round_tuple in format_data(input_data)
    ]  # type: ignore
    return sum(scored_rounds)


def part2(input_data):
    scored_rounds = [
        score_round2(round_tuple) for round_tuple in format_data(input_data)
    ]  # type: ignore
    return sum(scored_rounds)
