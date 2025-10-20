function getTuple(row) {
  const matches = row.match(/\d+/g);
  return [Number(matches[0]), Number(matches.slice(-1)[0])];
}

function part1(input) {
  rows = input.trim().split("\n").map(getTuple);
  left = rows.map((v) => v[0]).toSorted((a, b) => a - b);
  right = rows.map((v) => v[1]).toSorted((a, b) => a - b);
  zipped = left.map((l, i) => Math.abs(l - right[i]));
  return zipped.reduce((a, v) => a + v);
}

function countNums(input) {
  const map = new Map();

  for (const digit of input) {
    map.set(digit, (map.get(digit) ?? 0) + 1);
  }
  return map;
}

function part2(input) {
  rows = input.trim().split("\n").map(getTuple);
  left = rows.map((v) => v[0]);
  right = rows.map((v) => v[1]);
  rightCounts = countNums(right);
  values = left.map((num) =>
    rightCounts.has(num) ? num * rightCounts.get(num) : 0,
  );
  return values.reduce((a, v) => a + v);
}

module.exports = { part1, part2 };
