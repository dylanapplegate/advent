type RotationInstruction = [string, number];

function formatInput(input: string): RotationInstruction[] {
  return input.split('\n').map((line) => {
    const direction = line.slice(0, 1);
    const distance = Number(line.slice(1));
    return [direction, distance];
  });
}

export function part1(input: string): number | string | undefined {
  const rotations = formatInput(input);
  let value = 50;
  let zeroCount = 0;

  for (let [direction, distance] of rotations) {
    const distanceNormalized = distance % 100;

    if (direction === 'R') {
      value = (value + distanceNormalized) % 100;
    } else {
      value = (value - distanceNormalized + 100) % 100;
    }

    zeroCount += value === 0 ? 1 : 0;
  }

  return zeroCount;
}

export function part2(input: string): number | string | undefined {
  const rotations = formatInput(input);

  let value = 50;
  let zeroCount = 0;

  for (let [direction, distance] of rotations) {
    const additive = direction === 'L' ? -1 : 1;

    let counter = distance;

    while (counter > 0) {
      value += additive;

      if (value === -1) {
        value = 99;
      } else if (value === 100) {
        value = 0;
      }

      zeroCount += value === 0 ? 1 : 0;
      counter -= 1;
    }
  }

  return zeroCount;
}
