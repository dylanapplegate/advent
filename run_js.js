const { spawn } = require("child_process");
const fs = require("fs");
const path = require("path");
const chokidar = require("chokidar");

const [, , year, day] = process.argv;

if (!year || !day) {
  console.error("Usage: node run_js.js <YEAR> <DAY>");
  process.exit(1);
}

const dayPadded = `day${day.padStart(2, "0")}`;
const solutionPath = path.join(year, dayPadded, "javascript");

if (!fs.existsSync(solutionPath)) {
  console.error(`Error: Solution path not found at ${solutionPath}`);
  process.exit(1);
}

function runTestsAndSolution() {
  const testPattern = `${year}/${dayPadded}`;
  const jest = spawn("jest", ["--testNamePattern", testPattern], {
    stdio: "inherit",
  });

  jest.on("close", (code) => {
    if (code !== 0) {
      console.error("Tests Failed. Skipping final solution run.");
      return;
    }

    console.log("All tests passed!");

    const inputFilePath = path.join(year, dayPadded, "input.txt");
    const inputData = fs.readFileSync(inputFilePath, "utf-8");

    // Invalidate require cache to get the latest version of the solution
    delete require.cache[
      require.resolve(path.resolve(solutionPath, "solution.js"))
    ];
    const { part1, part2 } = require(path.resolve(solutionPath, "solution.js"));

    const part1Result = part1(inputData);
    const part2Result = part2(inputData);

    console.log(`Part 1: ${part1Result}`);
    console.log(`Part 2: ${part2Result}`);
  });
}

runTestsAndSolution();

const watcher = chokidar.watch(path.join(solutionPath, "solution.js"));

watcher.on("change", () => {
  process.stdout.write("\x1Bc");
  console.log("Solution file changed. Re-running tests...");
  runTestsAndSolution();
});
