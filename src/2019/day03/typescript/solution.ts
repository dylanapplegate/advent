const MOVE_DELTAS = {
  U: [1, 0],
  D: [-1, 0],
  R: [0, 1],
  L: [0, -1],
};

type Directions = Array<[string, number]>;

function formatWire(input: string): Directions {
  return input
    .trim()
    .split(',')
    .map((direction) => [direction.slice(0, 1), parseInt(direction.slice(1))]);
}

function formatData(input: string): [Directions, Directions] {
  const wires = input.split('\n').map(formatWire);

  if (wires.length !== 2) {
    throw new Error('Invalid length');
  }
  return wires as [Directions, Directions];
}

function getCoordKey(y: number, x: number): string {
  return `${y}:${x}`;
}

function getVisitedSet(directions: Directions): Set<string> {
  const visited: Set<string> = new Set();
  let y = 0,
    x = 0;

  for (const [direction, distance] of directions) {
    const [dy, dx] = MOVE_DELTAS[direction];

    for (let i = 0; i < distance; i++) {
      y += dy;
      x += dx;

      visited.add(getCoordKey(y, x));
    }
  }

  return visited;
}

function getStepsToIntersection(
  directions: Directions,
  intersections: Set<string>,
): Map<string, number> {
  const stepCount: Map<string, number> = new Map();
  let y = 0,
    x = 0;
  let steps = 0;

  for (const [direction, distance] of directions) {
    const [dy, dx] = MOVE_DELTAS[direction];

    for (let i = 0; i < distance; i++) {
      y += dy;
      x += dx;
      steps += 1;

      const coord = getCoordKey(y, x);

      if (intersections.has(coord) && !stepCount.has(coord)) {
        stepCount.set(coord, steps);
      }
    }
  }
  return stepCount;
}

export function part1(input: string): number | string | undefined {
  const wires = formatData(input);
  const visited1 = getVisitedSet(wires[0]);
  const visited2 = getVisitedSet(wires[1]);

  const intersections = visited1.intersection(visited2);

  const distances = [...intersections].map((coord) => {
    const [y, x] = coord.split(':').map(Number);

    return Math.abs(y) + Math.abs(x);
  });

  const minDistance = Math.min(...distances);

  return minDistance;
}

export function part2(input: string): number | string | undefined {
  const wires = formatData(input);
  const visited1 = getVisitedSet(wires[0]);
  const visited2 = getVisitedSet(wires[1]);

  const intersections = visited1.intersection(visited2);

  const steps1 = getStepsToIntersection(wires[0], intersections);
  const steps2 = getStepsToIntersection(wires[1], intersections);

  const stepCount = [...intersections].map(
    (intersection) => steps1.get(intersection) + steps2.get(intersection),
  );

  return Math.min(...stepCount);
}
