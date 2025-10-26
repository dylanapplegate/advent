export function part1(input: string): string {
  return input
    .split('')
    .reduce((total, digit, i, arr) => {
      const nextDigit = arr[(i + 1) % arr.length];
      return total + (digit === nextDigit ? parseInt(digit) : 0);
    }, 0)
    .toString();
}

export function part2(input: string): string {
  return input
    .split('')
    .reduce((total, digit, i, arr) => {
      const nextDigit = arr[(i + arr.length / 2) % arr.length];
      return total + (digit === nextDigit ? parseInt(digit) : 0);
    }, 0)
    .toString();
}
