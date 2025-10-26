function getTuple(row: string): [number, number] {
  const matches = row.match(/\d+/g);
  if (!matches) {
    return [0, 0];
  }
  return [Number(matches[0]), Number(matches.slice(-1)[0])];
}

export function part1(input: string): number {
  const rows = input.trim().split("\n").map(getTuple);
  const left = rows.map((v) => v[0]).sort((a, b) => a - b);
  const right = rows.map((v) => v[1]).sort((a, b) => a - b);
  const zipped = left.map((l, i) => Math.abs(l - right[i]));
  return zipped.reduce((a, v) => a + v);
}

function countNums(input: number[]): Map<number, number> {
  const map = new Map<number, number>();

  for (const digit of input) {
    map.set(digit, (map.get(digit) ?? 0) + 1);
  }
  return map;
}

export function part2(input: string): number {
  const rows = input.trim().split("\n").map(getTuple);
  const left = rows.map((v) => v[0]);
  const right = rows.map((v) => v[1]);
  const rightCounts = countNums(right);
  const values = left.map((num) =>
    rightCounts.has(num) ? num * (rightCounts.get(num) ?? 0) : 0,
  );
  return values.reduce((a, v) => a + v);
}
