function formatData(input: string): number[][] {
  return input
    .trim()
    .split('\n')
    .map((line) => line.trim().split(/\s+/g).map(Number));
}

function isValidTriangle(a: number, b: number, c: number): boolean {
  return a + b > c && a + c > b && c + b > a;
}

export function part1(input: string): number | string | undefined {
  const matrix = formatData(input);
  return matrix.filter(([a, b, c]) => isValidTriangle(a, b, c)).length;
}

export function part2(input: string): number | string | undefined {
  const matrix = formatData(input);
  let validTriangles = 0;

  for (let x = 0; x < matrix[0].length; x++) {
    for (let y = 0; y < matrix.length; y += 3) {
      const a = matrix[y][x];
      const b = matrix[y + 1][x];
      const c = matrix[y + 2][x];

      validTriangles += isValidTriangle(a, b, c) ? 1 : 0;
    }
  }

  return validTriangles;
}
