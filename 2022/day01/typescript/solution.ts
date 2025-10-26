function total(input: string): number {
  return input
    .split("\n")
    .map(Number)
    .reduce((acc, v) => acc + v);
}

export function part1(input: string): number {
  return input
    .split("\n\n")
    .map(total)
    .reduce((acc, v) => Math.max(acc, v));
}

export function part2(input: string): number {
  return input
    .split("\n\n")
    .map(total)
    .sort((a, b) => b - a)
    .filter((_, i) => i < 3)
    .reduce((acc, v) => acc + v);
}
