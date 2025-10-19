const { toWords } = require("number-to-words");

const wordToNumber = {};
Array.from({ length: 10 }, (v, i) => [toWords(i), i]).forEach(
  ([w, v]) => (wordToNumber[w] = v),
);

function part1(input) {
  const numbers = input.split("\n").map((v) => {
    const stringNum = (v.match(/[0-9]/g) ?? []).join("");
    const num = Number(stringNum[0] + stringNum.slice(-1));
    return num;
  });

  return numbers.reduce((acc, v) => acc + v);
}

function part2(input) {
  const numbers = input.split("\n").map((v) => {
    console.log({ wordToNumber });

    // for (const [key, value] in wordToNumber.entries()) {
    //   v.replace(key, value);
    // }
    const stringNum = (v.match(/[0-9]/g) ?? []).join("");
    const num = Number(stringNum[0] + stringNum.slice(-1));
    return num;
  });

  return numbers.reduce((acc, v) => acc + v);
}

module.exports = { part1, part2 };
