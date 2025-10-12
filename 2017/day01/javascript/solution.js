function part1(input) {
  return input
    .split("")
    .reduce((total, digit, i, arr) => {
      const nextDigit = arr[(i + 1) % arr.length];
      return total + (digit === nextDigit ? parseInt(digit) : 0);
    }, 0)
    .toString();
}

function part2(input) {
  return input
    .split("")
    .reduce((total, digit, i, arr) => {
      const nextDigit = arr[(i + arr.length / 2) % arr.length];
      return total + (digit === nextDigit ? parseInt(digit) : 0);
    }, 0)
    .toString();
}

module.exports = { part1, part2 };
