import { format } from 'path';

function formatInput(input: string): string[] {
  return input
    .trim()
    .split('\n')
    .map((line) => line.trim());
}

function getCharPriority(char: string): number {
  const charCode = char.charCodeAt(0);

  if ('a'.charCodeAt(0) <= charCode && charCode <= 'z'.charCodeAt(0)) {
    return charCode - 'a'.charCodeAt(0) + 1;
  } else {
    return charCode - 'A'.charCodeAt(0) + 1 + 26;
  }
}

export function part1(input: string): number | string | undefined {
  const backpacks = formatInput(input);
  const commonalities = backpacks.map((backpack) => {
    const mid = Math.floor(backpack.length / 2);
    const leftSet = new Set(backpack.slice(0, mid));
    const rightSet = new Set(backpack.slice(mid));

    const commonality = leftSet.intersection(rightSet);
    return [...commonality];
  });
  const priorities = commonalities.map((common) => {
    return common.reduce((acc, char) => acc + getCharPriority(char), 0);
  });
  const sum = priorities.reduce((acc, priority) => acc + priority, 0);
  return sum;
}

export function part2(input: string): number | string | undefined {
  const backpacks = formatInput(input);
  let priorities = 0;
  for (let i = 0; i < backpacks.length; i += 3) {
    let intersect = new Set(backpacks[i + 0]);
    intersect = intersect.intersection(new Set(backpacks[i + 1]));
    intersect = intersect.intersection(new Set(backpacks[i + 2]));
    priorities += [...intersect]
      .map((char) => getCharPriority(char))
      .reduce((acc, num) => acc + num, 0);
  }
  return priorities;
}
