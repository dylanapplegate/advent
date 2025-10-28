const moveDelta: Record<string, [number, number]> = {
  '^': [-1, 0],
  '>': [0, 1],
  v: [1, 0],
  '<': [0, -1],
};

function getSetKey(y: number, x: number): string {
  return `${y},${x}`;
}

export function part1(moves: string): number | string | undefined {
  let y = 0;
  let x = 0;
  const visited = new Set([getSetKey(y, x)]);

  for (const move of moves) {
    const [dy, dx] = moveDelta[move];
    y += dy;
    x += dx;
    visited.add(getSetKey(y, x));
  }

  return visited.size;
}

export function part2(moves: string): number | string | undefined {
  const moversPos = [
    [0, 0],
    [0, 0],
  ];
  const visited = new Set([getSetKey(0, 0)]);

  for (const [i, move] of moves.split('').entries()) {
    const moverI = i % 2;

    let [y, x] = moversPos[moverI];
    const [dy, dx] = moveDelta[move];

    y += dy;
    x += dx;

    moversPos[moverI] = [y, x];
    visited.add(getSetKey(y, x));
  }

  return visited.size;
}
