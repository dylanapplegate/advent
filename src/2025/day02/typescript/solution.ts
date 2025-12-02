type ProductIdRange = [string, string];

function formatInput(input: string): ProductIdRange[] {
  return input.split(',').map((range) => {
    const splitRanges = range.split('-');
    return [splitRanges[0], splitRanges[1]];
  });
}

function getInvalidSingleIds(lower: number, upper: number) {}

export function part1(input: string): number | string | undefined {
  return undefined;
}

export function part2(input: string): number | string | undefined {
  return undefined;
}
