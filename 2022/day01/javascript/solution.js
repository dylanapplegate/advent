function total(input) {
  return input
    .split("\n")
    .map(Number)
    .reduce((acc, v) => acc + v);
}

function part1(input) {
  return input
    .split("\n\n")
    .map(total)
    .reduce((acc, v) => Math.max(acc, v));
}

function part2(input) {
  return input
    .split("\n\n")
    .map(total)
    .toSorted((a, b) => b - a)
    .filter((_, i) => i < 3)
    .reduce((acc, v) => acc + v);
}

module.exports = { part1, part2 };
