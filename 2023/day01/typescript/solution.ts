import { toWords } from 'number-to-words';

const wordToNumber: Record<string, number> = {};
Array.from({ length: 9 }, (v, i) => [toWords(i + 1), i + 1]).forEach(
  ([w, v]) => {
    wordToNumber[w as string] = v as number;
    wordToNumber[v as string] = v as number;
  },
);

export function part1(input: string): number {
  const numbers = input.split('\n').map((v) => {
    const stringNum = (v.match(/[0-9]/g) ?? []).join('');
    const num = Number(stringNum[0] + stringNum.slice(-1));
    return num;
  });

  return numbers.reduce((acc, v) => acc + v);
}

function getFirstAndLast(input: string): number {
  let firstIndex = Infinity;
  let lastIndex = -1;
  let firstMatch: string | null = null;
  let lastMatch: string | null = null;

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

  if (!firstMatch || !lastMatch) {
    return 0;
  }

  const firstMatchValue = wordToNumber[firstMatch];
  const lastMatchValue = wordToNumber[lastMatch];

  const firstLastTogether = Number(
    firstMatchValue.toString() + lastMatchValue.toString(),
  );

  return firstLastTogether;
}

export function part2(input: string): number {
  return input
    .split('\n')
    .map((v) => getFirstAndLast(v))
    .reduce((acc, value) => acc + value);
}
