function _prepareMoves(input_data: string | number[]): number[] {
  if (Array.isArray(input_data)) {
    return input_data.map((v) => parseInt(v.toString().trim()));
  }

  return input_data
    .trim()
    .split("\n")
    .map((v) => parseInt(v.trim()));
}

export function part1(input_data: string): number {
  const moves = _prepareMoves(input_data);
  const total = moves.reduce((sum, move) => sum + move, 0);

  return total;
}

export function part2(input_data: string): number {
  const moves = _prepareMoves(input_data);

  let total = 0;
  const seen = new Set<number>();
  seen.add(0);

  while (true) {
    for (const move of moves) {
      total += move;

      if (seen.has(total)) {
        return total;
      }

      seen.add(total);
    }
  }
}
