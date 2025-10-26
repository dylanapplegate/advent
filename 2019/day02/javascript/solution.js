function formatInput(input) {
  return input.split(",").map(Number);
}

function part1(input) {
  const program = formatInput(input);

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

function part2(input) {
  return undefined;
}

module.exports = { part1, part2 };
