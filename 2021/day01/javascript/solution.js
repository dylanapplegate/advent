function formatInput(input) {
  return input.split("\n").map(Number);
}
function part1(input) {
  input = formatInput(input);
  return input.reduce((acc, v, i, a) => {
    if (i === 0) {
      return acc;
    }
    const difference = a[i] - a[i - 1];

    if (difference > 0) {
      return acc + 1;
    }
    return acc;
  }, 0);
}

function part2(input) {
  input = formatInput(input);
  return input.reduce((acc, v, i, a) => {
    if (i < 3) {
      return acc;
    }
    const difference = a[i] - a[i - 3];

    if (difference > 0) {
      return acc + 1;
    }
    return acc;
  }, 0);
}

module.exports = { part1, part2 };
