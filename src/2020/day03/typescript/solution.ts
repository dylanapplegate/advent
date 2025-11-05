function formatInput(input: string): string[][] {
  return input
    .trim()
    .split('\n')
    .filter((l) => l.trim())
    .map((line) => line.split(''));
}

type Coordinate = [number, number];

function* iterateOnSlope(dr: number, dc: number): IterableIterator<Coordinate> {
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

  let treeCount = 0;

  const generator = iterateOnSlope(rise, run);
  let coords = generator.next();

  while (!coords.done) {
    let [y, x] = !coords.done ? coords.value! : [null, null];

    if (y == null || x == null) {
      break;
    }

    x %= colsN;

    if (y >= rowsN) {
      break;
    }

    treeCount += area[y][x] === '#' ? 1 : 0;

    coords = generator.next();
  }

  return treeCount;
}

export function part1(input: string): number | string | undefined {
  const area = formatInput(input);
  return getTreeCount(area, 1, 3);
}

export function part2(input: string): number | string | undefined {
  const area = formatInput(input);
  const slopes = [
    [1, 1],
    [1, 3],
    [1, 5],
    [1, 7],
    [2, 1],
  ];

  return slopes
    .map(([y, x]) => getTreeCount(area, y, x))
    .reduce((prod, num) => prod * num);
}
