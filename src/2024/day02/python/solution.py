from typing import List


def format_input_data(input: str) -> List[List[int]]:
    lines = [
        [int(level) for level in line.strip().split(" ")]
        for line in input.strip().split("\n")
    ]
    return lines


def is_safe(report: List[int]) -> bool:
    diffs = [l_level - r_level for l_level, r_level in zip(report, report[1:])]
    return all(diff < 0 and abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs) or all(
        diff > 0 and abs(diff) >= 1 and abs(diff) <= 3 for diff in diffs
    )


def is_safe_with_single_exception(report: List[int]) -> bool:
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1 :]):
            return True

    return False

def part1(input_data: str) -> int:
    reports = format_input_data(input_data)
    is_safe_reports = [is_safe(report) for report in reports]
    safe_report_count = len([is_safe for is_safe in is_safe_reports if is_safe])
    return safe_report_count

def part2(input_data: str) -> int:
    reports = format_input_data(input_data)
    is_safe_reports = [is_safe_with_single_exception(report) for report in reports]
    safe_report_count = len([is_safe for is_safe in is_safe_reports if is_safe])
    return safe_report_count
