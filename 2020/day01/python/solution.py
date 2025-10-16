from typing import Union, List, Optional
TOTAL = 2020


def _formatInput(input_data: Union[str, List[str]]) -> List[int]:
    if isinstance(input_data, str):
        input_data = [line.strip() for line in input_data.strip().split('\n')
                      if line.strip()]

    return [int(v) for v in input_data]


def part1(input_data):
    expenses = _formatInput(input_data)
    seen = set()

    for expense in expenses:
        complement = TOTAL - expense

        if complement in seen:
            return str(expense * complement)

        seen.add(expense)

    return None
def part2(input_data):
    expenses = sorted(_formatInput(input_data))
    N = len(expenses)

    for i in range(N - 2):
        complement = TOTAL - expenses[i]
        l = i + 1
        r = N - 1

        while(l < r):
            subtotal = expenses[l] + expenses[r]
            if subtotal == complement:
                return str(expenses[i] * expenses[l] * expenses[r])
            elif subtotal < complement:
                l+=1
            else:
                r-=1

    return None