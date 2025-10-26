function formatInput(input: string): string[] {
  return input.trim().split('\n');
}

function countLine(line: string): [number, number] {
  const counts = new Map<string, number>();
  for (const c of line) {
    counts.set(c, (counts.get(c) ?? 0) + 1);
  }
  const values = [...counts.values()];
  const hasThree = values.includes(3);
  const hasTwo = values.includes(2);

  return [hasThree ? 1 : 0, hasTwo ? 1 : 0];
}

function getDuplicate(ids: string[]): string {
  const seen = new Set<string>();

  for (const id of ids) {
    if (seen.has(id)) {
      return id;
    }
    seen.add(id);
  }
  return '';
}

export function part1(input: string): number {
  const ids = formatInput(input);
  const countedIds = ids.map((line) => countLine(line));
  const sums = countedIds.reduce(
    (acc, count) => {
      acc[0] += count[0];
      acc[1] += count[1];
      return acc;
    },
    [0, 0],
  );
  return sums.reduce((a, v) => a * v);
}

export function part2(input: string): string {
  const ids = formatInput(input);

  for (let i = 0; i < ids[0].length; i++) {
    const subbedIds = ids.map((id) => id.slice(0, i) + id.slice(i + 1));
    const duplicate = getDuplicate(subbedIds);
    if (duplicate !== '') {
      return duplicate;
    }
  }

  return '';
}
