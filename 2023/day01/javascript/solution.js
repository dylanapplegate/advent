const { toWords } = require("number-to-words");

const wordToNumber = {};
Array.from({ length: 9 }, (v, i) => [toWords(i + 1), i + 1]).forEach(
  ([w, v]) => {
    wordToNumber[w] = v;
    wordToNumber[v] = v;
  },
);

function part1(input) {
  const numbers = input.split("\n").map((v) => {
    const stringNum = (v.match(/[0-9]/g) ?? []).join("");
    const num = Number(stringNum[0] + stringNum.slice(-1));
    return num;
  });

  return numbers.reduce((acc, v) => acc + v);
}

function getFirstAndLast(input) {
  let firstIndex = Infinity;
  let lastIndex = -1;
  let firstMatch = null;
  let lastMatch = null;

  for (let term of Object.keys(wordToNumber)) {
    const firstTermIndex = input.indexOf(term);
    if (firstTermIndex !== -1 && firstTermIndex < firstIndex) {
      firstIndex = firstTermIndex;
      firstMatch = term;
    }

    const lastTermIndex = input.lastIndexOf(term);
    if (lastTermIndex !== -1 && input.lastIndexOf(term) > lastIndex) {
      lastIndex = input.lastIndexOf(term);
      lastMatch = term;
    }
  }

  const firstMatchValue = wordToNumber[firstMatch];
  const lastMatchValue = wordToNumber[lastMatch];

  const firstLastTogether = Number(
    firstMatchValue.toString() + lastMatchValue.toString(),
  );

  return firstLastTogether;
}

function part2(input) {
  return input
    .split("\n")
    .map((v) => getFirstAndLast(v))
    .reduce((acc, value) => acc + value);
}

module.exports = { part1, part2 };
