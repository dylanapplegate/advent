function formatInput(input: string): number[] {
  return input.split("\n").map(Number);
}
export function part1(input: string): number {
  const parsedInput = formatInput(input);
  return parsedInput.reduce((acc, v, i, a) => {
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

export function part2(input: string): number {
  const parsedInput = formatInput(input);
  return parsedInput.reduce((acc, v, i, a) => {
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
