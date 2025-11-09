/* eslint-disable @typescript-eslint/no-loop-func */
function formatData(input: string): number[][] {
  return input.split('\n').map((line) => line.split('').map(Number));
}

export function part1(input: string): number | string | undefined {
  const ratings = formatData(input);

  const totals = ratings[0].map((v, i) => {
    return ratings.map((rating) => rating[i]).reduce((acc, num) => acc + num);
  });

  const mid = ratings.length / 2;

  let most = [];
  let min = [];

  for (const total of totals) {
    if (total > mid) {
      most.push(1);
      min.push(0);
    } else {
      most.push(0);
      min.push(1);
    }
  }
  const mostValue = parseInt(most.join(''), 2);
  const minValue = parseInt(min.join(''), 2);
  return mostValue * minValue;
}

export function part2(input: string): number | string | undefined {
  const ratings = formatData(input);

  let potentials = [...ratings];
  let currentIndex = 0;

  let min = [],
    max = [];

  while (potentials.length > 1) {
    const currentTotal = potentials
      .map((potential) => potential[currentIndex])
      .reduce((sum, num) => num + sum);

    const currentMid = potentials.length / 2;

    if (currentTotal >= currentMid) {
      max.push(1);
    } else {
      max.push(0);
    }

    potentials = potentials.filter(
      (potential) => potential[currentIndex] === max.at(-1),
    );
    currentIndex++;
  }

  max = potentials[0];

  potentials = [...ratings];
  currentIndex = 0;
  while (potentials.length > 1) {
    const currentTotal = potentials
      .map((potential) => potential[currentIndex])
      .reduce((sum, num) => num + sum);

    const currentMid = potentials.length / 2;

    if (currentTotal >= currentMid) {
      min.push(0);
    } else {
      min.push(1);
    }

    potentials = potentials.filter(
      (potential) => potential[currentIndex] === min.at(-1),
    );

    currentIndex++;
  }

  min = potentials[0];

  const maxValue = parseInt(max.join(''), 2);
  const minValue = parseInt(min.join(''), 2);
  return maxValue * minValue;
}
