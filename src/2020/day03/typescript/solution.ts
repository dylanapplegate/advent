function formatInput(input: string): string[][] {
  return input
    .trim()
    .split('\n')
    .filter((l) => l.trim())
    .map((line) => line.split(''));
}

function getGCD(a: number, b: number): number {
  return b === 0 ? a : getGCD(b, a % b);
}

type Coordinate = [number, number];

function* iterateOnSlope(
  dr: number,
  dc: number,
): Generator<Coordinate, void, void> {
  let currentY = 0,
    currentX = 0;

  while (true) {
    currentY += dr;
    currentX += dc;
    yield [currentY, currentX];
  }
}

function getTreeCount(area: string[][], rise: number, run: number): number {
  if (!area || !area.length || !area[0].length) {
    return 0;
  }
  const rowsN = area.length;
  const colsN = area[0].length;

  let y = 0,
    x = 0;

  let treeCount = 0;

  const generator = iterateOnSlope(rise, run);

  while (y < rowsN) {
    const [dy, dx] = generator.next().value;
    y += dy;
    x += dx;
    x %= colsN;

    treeCount += area[y][x] === '#' ? 1 : 0;
  }

  return treeCount;
}

export function part1(input: string): number | string | undefined {
  const area = formatInput(input);
  return getTreeCount(area, 1, 3);
}

export function part2(input: string): number | string | undefined {
  return undefined;
}
