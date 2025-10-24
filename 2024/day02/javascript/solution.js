function formatInputData(data) {
  return data.split("\n").map((line) => line.split(" ").map(Number));
}

function isSafe(report) {
  const diffs = report
    .slice(0, report.length - 1)
    .map((level, i) => report[i + 1] - level);

  const ascendingSafe = diffs.every(
    (diff) => diff > 0 && Math.abs(diff) >= 1 && Math.abs(diff) <= 3,
  );
  const descendingSafe = diffs.every(
    (diff) => diff < 0 && Math.abs(diff) >= 1 && Math.abs(diff) <= 3,
  );

  return ascendingSafe || descendingSafe;
}

function isSafeWithException(report) {
  for (let i = 0; i < report.length; i++) {
    if (isSafe([...report.slice(0, i), ...report.slice(i + 1)])) {
      return true;
    }
  }
  return false;
}

function part1(input) {
  const reports = formatInputData(input);
  const safeReportCount = reports.filter((report) => isSafe(report)).length;
  return safeReportCount;
}

function part2(input) {
  const reports = formatInputData(input);
  const safeReportCount = reports.filter((report) =>
    isSafeWithException(report),
  ).length;
  return safeReportCount;
}

module.exports = { part1, part2 };
