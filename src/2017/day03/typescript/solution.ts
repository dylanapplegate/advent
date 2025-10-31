function formatData(input: string): number[][] {
  return input
    .trim()
    .split('\n')
    .map((line) => line.trim().split(/\s/g).map(Number));
}

export function part1(input: string): number | string | undefined {
  return formatData(input)
    .map((line) => Math.max(...line) - Math.min(...line))
    .reduce((acc, num) => acc + num, 0);
}

function getEvenDivisor(nums: number[]): number {
  nums.sort((a, b) => b - a);
  const N = nums.length;

  for (let l = 0; l < N; l++) {
    for (let r = l + 1; r < N; r++) {
      const numLeft = nums[l];
      const numRight = nums[r];

      if (numLeft % numRight === 0) {
        return numLeft / numRight;
      }
    }
  }
}

export function part2(input: string): number | string | undefined {
  return formatData(input)
    .map((line) => getEvenDivisor(line))
    .reduce((acc, num) => acc + num);
}
