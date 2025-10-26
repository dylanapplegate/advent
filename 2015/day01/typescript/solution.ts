export function part1(input: string): string {
  return input
    .split('')
    .map((v) => (v === '(' ? 1 : -1))
    .reduce((a, b) => a + b, 0)
    .toString();
}

export function part2(input: string): string | undefined {
  const map: Record<string, number> = {
    '(': 1,
    ')': -1,
  };
  let sum = 0;
  for (let i = 0; i < input.length; i++) {
    sum += map[input[i]];
    if (sum === -1) {
      return (i + 1).toString();
    }
  }
  return undefined;
}
