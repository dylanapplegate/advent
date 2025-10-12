function _prepareMoves(input_data) {
  if (Array.isArray(input_data)) {
    return input_data.map((v) => parseInt(v.trim()));
  }

  return input_data
    .trim()
    .split("\n")
    .map((v) => parseInt(v.trim()));
}

function part1(input_data) {
  const moves = _prepareMoves(input_data);

  const total = moves.reduce((sum, move) => sum + move, 0);

  return total.toString();
}

function part2(input_data) {
  const moves = _prepareMoves(input_data);

  let total = 0;
  const seen = new Set();
  seen.add(0);

  while (true) {
    for (const move of moves) {
      total += move;

      if (seen.has(total)) {
        return total.toString();
      }

      seen.add(total);
    }
  }
}

module.exports = { part1, part2 };
