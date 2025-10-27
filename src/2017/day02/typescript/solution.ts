function formatInput(input: string): number[][] {
  return input.split('\n').map((row) => row.split(/\s+/g).map(Number));
}

export function part1(input: string): number | string | undefined {
  const rows = formatInput(input);
  const differences = rows.map((row) => Math.max(...row) - Math.min(...row));
  return differences.reduce((sum, num) => sum + num);
}

function getEvenDivision(row: number[]): number {
  for (let l = 0; l < row.length; l++) {
    for (let r = l + 1; r < row.length; r++) {
      if (row[l] % row[r] === 0) {
        return row[l] / row[r];
      }
      if (row[r] % row[l] === 0) {
        return row[r] / row[l];
      }
    }
  }
  return 0;
}

export function part2(input: string): number | string | undefined {
  const divisors = formatInput(input).map((row) => getEvenDivision(row));
  return divisors.reduce((sum, divisor) => sum + divisor);
}
