function calculateFuel(mass: number): number {
  return Math.floor(mass / 3) - 2;
}

function calculateRecursiveFuel(mass: number): number {
  const fuel = Math.floor(mass / 3) - 2;
  if (fuel <= 0) return 0;
  return fuel + calculateRecursiveFuel(fuel);
}

export function part1(input: string): string {
  if (input.includes('\n')) {
    return input
      .split('\n')
      .map((a) => calculateFuel(parseInt(a)))
      .reduce((a, b) => a + b, 0)
      .toString();
  }
  return (Math.floor(Number(input) / 3) - 2).toString();
}

export function part2(input: string): string {
  if (input.includes('\n')) {
    return input
      .split('\n')
      .map((a) => calculateRecursiveFuel(parseInt(a)))
      .reduce((a, b) => a + b, 0)
      .toString();
  }
  return (Math.floor(Number(input) / 3) - 2).toString();
}
