const shapes: Record<string, string> = {
  A: "Rock",
  B: "Paper",
  C: "Scissors",
  X: "Rock",
  Y: "Paper",
  Z: "Scissors",
};

const beats: Record<string, string> = { Rock: "Scissors", Scissors: "Paper", Paper: "Rock" };
const loses: Record<string, string> = { Rock: "Paper", Scissors: "Rock", Paper: "Scissors" };
const scores: Record<string, number> = { Rock: 1, Paper: 2, Scissors: 3 };

function formatData(input: string): string[][] {
  return input
    .trim()
    .split("\n")
    .map((line) => line.trim().split(" "));
}

function scoreRound(round: string[]): number {
  const [opponent, self] = round;
  let score = scores[shapes[self]];
  if (beats[shapes[self]] === shapes[opponent]) {
    score += 6;
  } else if (shapes[self] == shapes[opponent]) {
    score += 3;
  }
  return score;
}

function scoreRound2(round: string[]): number {
  const [shape, result] = round;
  const mappedShape = shapes[shape];
  if (result === "X") {
    return scores[beats[mappedShape]];
  } else if (result === "Y") {
    return 3 + scores[mappedShape];
  } else {
    return 6 + scores[loses[mappedShape]];
  }
}

export function part1(input: string): number {
  const scoredRounds = formatData(input).map((round) => scoreRound(round));
  return scoredRounds.reduce((total, score) => total + score, 0);
}

export function part2(input: string): number {
  const scoredRounds = formatData(input).map((round) => scoreRound2(round));
  return scoredRounds.reduce((total, score) => total + score, 0);
}
