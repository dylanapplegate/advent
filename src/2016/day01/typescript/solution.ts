interface State {
  x: number;
  y: number;
  dir: number;
}

export function part1(input: string): number {
  const directions: [number, number][] = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  const initialState: State = { x: 0, y: 0, dir: 0 };

  const sequence = input.split(',').map((s) => s.trim());

  const finalState = sequence.reduce((state, move) => {
    const turn = move[0];
    const distance = parseInt(move.slice(1));

    let newDir = state.dir;
    if (turn === 'R') {
      newDir = (newDir + 1) % 4;
    } else if (turn === 'L') {
      newDir = (newDir + 3) % 4;
    }

    const [dx, dy] = directions[newDir];

    return {
      x: state.x + dx * distance,
      y: state.y + dy * distance,
      dir: newDir,
    };
  }, initialState);

  return Math.abs(finalState.x) + Math.abs(finalState.y);
}

export function part2(input: string): number | undefined {
  const directions: [number, number][] = [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0],
  ];

  const visited = new Set<string>();

  const sequence = input.split(',').map((s) => s.trim());
  let direction = 0;

  let y = 0;
  let x = 0;

  for (let move of sequence) {
    const turn = move[0];
    const distance = parseInt(move.slice(1));

    if (turn === 'R') {
      direction = (direction + 1) % 4;
    } else if (turn === 'L') {
      direction = (direction + 3) % 4;
    }

    const [dx, dy] = directions[direction];
    for (let i = 0; i < distance; i++) {
      x += dx;
      y += dy;

      if (visited.has(`${x},${y}`)) {
        return Math.abs(x) + Math.abs(y);
      }

      visited.add(`${x},${y}`);
    }
  }
}
