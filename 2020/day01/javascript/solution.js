function part1(input) {
  const expenses = formatInput(input);
  const seen = new Set();
  for (const expense of expenses) {
    const rem = 2020 - expense;
    if (seen.has(rem)) {
      return expense * rem;
    }
    seen.add(expense);
  }
  return undefined;
}

function formatInput(input) {
  return input.split("\n").map(Number);
}

function part2(input) {
  const expenses = formatInput(input).sort((a, b) => a - b);

  for (let i = 0; i < expenses.length - 2; i += 1) {
    const rem = 2020 - expenses[i];
    let l = i + 1;
    let r = expenses.length - 1;

    while (l < r) {
      const subTotal = expenses[l] + expenses[r];
      if (subTotal === rem) {
        return expenses[i] * expenses[l] * expenses[r];
      } else if (subTotal < rem) {
        l++;
      } else {
        r--;
      }
    }
  }
  return undefined;
}

module.exports = { part1, part2 };
