const shapes = {
  A: "Rock",
  B: "Paper",
  C: "Scissors",
  X: "Rock",
  Y: "Paper",
  Z: "Scissors",
};

const beats = { Rock: "Scissors", Scissors: "Paper", Paper: "Rock" };

const scores = { Rock: 1, Paper: 2, Scissors: 3 };

function formatData(input) {
  return input
    .trim()
    .split("\n")
    .map((line) => line.trim().split(" "));
}

function scoreRound(round) {
  const [opponent, self] = round;
  score = scores[shapes[self]];
  if (beats[shapes[self]] === shapes[opponent]) {
    score += 6;
  } else if (shapes[self] == shapes[opponent]) {
    score += 3;
  }
  return score;
}

function part1(input) {
  const scoredRounds = formatData(input).map((round) => scoreRound(round));
  return scoredRounds.reduce((total, score) => total + score, 0);
}

function part2(input) {
  return undefined;
}

module.exports = { part1, part2 };
