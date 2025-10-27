const PAD = [
  ['1', '2', '3'],
  ['4', '5', '6'],
  ['7', '8', '9'],
];
const COMPLEX_PAD = [
  ['x', 'x', '1', 'x', 'x'],
  ['x', '2', '3', '4', 'x'],
  ['5', '6', '7', '8', '9'],
  ['x', 'A', 'B', 'C', 'x'],
  ['x', 'x', 'D', 'x', 'x'],
];

const DIRECTION_MAP = { U: [-1, 0], R: [0, 1], D: [1, 0], L: [0, -1] };

function formatData(input: string): string[] {
  return input.trim().split('\n');
}

function isValidSimple(y: number, x: number): boolean {
  return 0 <= y && y <= 2 && 0 <= x && x <= 2;
}

function isValidComplex(y: number, x: number): boolean {
  return 0 <= y && y <= 4 && 0 <= x && x <= 4 && COMPLEX_PAD[y][x] !== 'x';
}

function solve(
  input: string,
  pad: string[][],
  isValid: (y: number, x: number) => boolean,
  startY: number,
  startX: number,
): string {
  const instructions = formatData(input);
  let code = '',
    y = startY,
    x = startX;

  for (const instruction of instructions) {
    for (const move of instruction) {
      const [dY, dX] = DIRECTION_MAP[move];
      const nY = y + dY,
        nX = x + dX;
      if (isValid(nY, nX)) {
        y = nY;
        x = nX;
      }
    }
    code += pad[y][x];
  }

  return code;
}

export function part1(input: string): number | string | undefined {
  return solve(input, PAD, isValidSimple, 1, 1);
}

export function part2(input: string): number | string | undefined {
  return solve(input, COMPLEX_PAD, isValidComplex, 2, 0);
}
