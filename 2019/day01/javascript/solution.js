function calculateFuel(mass) {
  return Math.floor(mass / 3) - 2;
}

function calculateRecursiveFuel(mass) {
  const fuel = Math.floor(mass / 3) - 2;
  if (fuel <= 0) return 0;
  return fuel + calculateRecursiveFuel(fuel);
}

function part1(input) {
  if (input.includes("\n")) {
    return input
      .split("\n")
      .map((a) => calculateFuel(parseInt(a)))
      .reduce((a, b) => a + b, 0)
      .toString();
  }
  return (Math.floor(input / 3) - 2).toString();
}

function part2(input) {
  if (input.includes("\n")) {
    return input
      .split("\n")
      .map((a) => calculateRecursiveFuel(parseInt(a)))
      .reduce((a, b) => a + b, 0)
      .toString();
  }
  return (Math.floor(input / 3) - 2).toString();
}

module.exports = { part1, part2 };
