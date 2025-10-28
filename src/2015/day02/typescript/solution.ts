type Dimensions = number[];

function formatInput(input: string): Dimensions[] {
  return input
    .trim()
    .split('\n')
    .map((line) => line.trim().split('x').map(Number));
}

function calculatePaper(dimensions: Dimensions): number {
  const [l, w, h] = dimensions;

  const sides = [l * w, w * h, h * l];
  const minSide = Math.min(...sides);

  const totalSurfaceArea = 2 * (sides[0] + sides[1] + sides[2]);

  return minSide + totalSurfaceArea;
}

function calculateRibbon(dimensions: Dimensions): number {
  const sortedDims = dimensions.toSorted((a, b) => a - b);
  const faceRibbon = 2 * (sortedDims[0] + sortedDims[1]);
  const bowRibbon = dimensions.reduce((prod, dimension) => prod * dimension, 1);
  return faceRibbon + bowRibbon;
}

export function part1(input: string): number | string | undefined {
  const totalPaper = formatInput(input)
    .map((row) => calculatePaper(row))
    .reduce((sum, num) => sum + num, 0);
  return totalPaper;
}

export function part2(input: string): number | string | undefined {
  const totalRibbon = formatInput(input)
    .map((row) => calculateRibbon(row))
    .reduce((sum, num) => sum + num, 0);
  return totalRibbon;
}
