function formatData(input) {
  return input
    .trim()
    .split("\n")
    .map((line) => {
      const splitValues = line.trim().split(/\s+/g);
      return [splitValues[0], Number(splitValues[1])];
    });
}

function part1(input) {
  let depth = 0,
    position = 0;
  const commands = formatData(input);
  for (const [direction, units] of commands) {
    if (direction === "forward") position += units;
    else if (direction === "up") depth -= units;
    else depth += units;
  }

  return depth * position;
}

function part2(input) {
  let depth = 0,
    position = 0,
    aim = 0;
  const commands = formatData(input);
  for (const [direction, units] of commands) {
    if (direction === "forward") {
      position += units;
      depth += units * aim;
    } else if (direction === "up") {
      aim -= units;
    } else {
      aim += units;
    }
  }

  return depth * position;
}

module.exports = { part1, part2 };
