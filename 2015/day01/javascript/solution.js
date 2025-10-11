function part1(input) {
  return input
    .split("")
    .map((v) => (v === "(" ? 1 : -1))
    .reduce((a, b) => a + b, 0)
    .toString();
}

function part2(input) {
  return undefined;
}

module.exports = { part1, part2 };
