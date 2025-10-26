function formatInput(input: string): number[] {
  return input.split(",").map(Number);
}

export function part1(input: string, skipSub = false): number {
  const program = formatInput(input);

  if (program[1] !== 9 && !skipSub) {
    program[1] = 12;
    program[2] = 2;
  }

  for (let o = 0; o < program.length; o += 4) {
    const optcode = program[o];

    if (optcode === 99) break;

    const r1 = program[o + 1];
    const r2 = program[o + 2];
    const i = program[o + 3];

    if (optcode === 1) {
      program[i] = program[r1] + program[r2];
    } else if (optcode === 2) {
      program[i] = program[r1] * program[r2];
    }
  }
  return program[0];
}

export function part2(input: string): number | undefined {
  const DESIRED_OUTCOME = 19690720;

  for (let i = 0; i < 100; i++) {
    for (let j = 0; j < 100; j++) {
      const program = formatInput(input);
      program[1] = i;
      program[2] = j;

      if (DESIRED_OUTCOME === part1(program.join(","), true))
        return 100 * i + j;
    }
  }
}
