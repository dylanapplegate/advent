function formatInput(input) {
  return input.trim().split("\n");
}

function countLine(line) {
  const counts = new Map();
  for (const c of line) {
    counts.set(c, (counts.get(c) ?? 0) + 1);
  }
  const values = [...counts.values()];
  const hasThree = values.includes(3);
  const hasTwo = values.includes(2);

  return [hasThree ? 1 : 0, hasTwo ? 1 : 0];
}

function getDuplicate(ids) {
  const seen = new Set();

  for (const id of ids) {
    if (seen.has(id)) {
      return id;
    }
    seen.add(id);
  }
  return "";
}

function part1(input) {
  const ids = formatInput(input);
  const countedIds = ids.map((line) => countLine(line));
  const sums = countedIds.reduce((acc, count) => {
    acc[0] += count[0];
    acc[1] += count[1];
    return acc;
  });
  return sums.reduce((a, v) => a * v);
}

function part2(input) {
  const ids = formatInput(input);

  for (let i = 0; i < ids[0].length; i++) {
    subbedIds = ids.map((id) => id.slice(0, i) + id.slice(i + 1));
    duplicate = getDuplicate(subbedIds);
    if (duplicate !== "") {
      return duplicate;
    }
  }

  return "";
}

module.exports = { part1, part2 };
