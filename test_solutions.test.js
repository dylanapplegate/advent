const fs = require("fs");
const path = require("path");

function findSolutionFiles(dir) {
  let solutionFiles = [];
  const files = fs.readdirSync(dir);

  for (const file of files) {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);

    if (stat.isDirectory()) {
      if (file !== "node_modules" && file !== ".venv" && file !== ".git") {
        solutionFiles = solutionFiles.concat(findSolutionFiles(filePath));
      }
    } else if (filePath.endsWith(path.join("javascript", "solution.js"))) {
      solutionFiles.push(filePath);
    }
  }
  return solutionFiles;
}

const solutionPaths = findSolutionFiles(process.cwd());

solutionPaths.forEach((solutionPath) => {
  const solutionDir = path.dirname(solutionPath);
  const dayDir = path.dirname(solutionDir);
  const relativePath = path.relative(process.cwd(), solutionPath);

  describe(relativePath, () => {
    const solution = require(solutionPath);
    const part1 = solution.part1;
    const part2 = solution.part2;

    const testDataPath = path.join(dayDir, "test_data.json");
    if (fs.existsSync(testDataPath)) {
      const testData = JSON.parse(fs.readFileSync(testDataPath, "utf-8"));

      if (part1 && testData.part1 && testData.part1.length > 0) {
        test("Part 1 JSON", () => {
          for (const { input, expected } of testData.part1) {
            expect(part1(input)).toBe(expected);
          }
        });
      }

      if (part2 && testData.part2 && testData.part2.length > 0) {
        test("Part 2 JSON", () => {
          for (const { input, expected } of testData.part2) {
            expect(part2(input)).toBe(expected);
          }
        });
      }
    }

    const exampleDataPath = path.join(dayDir, "example_1.txt");
    if (fs.existsSync(exampleDataPath)) {
      const content = fs.readFileSync(exampleDataPath, "utf-8").trim();
      const part1Match = content.match(
        /--- Part 1 ---\nInput:\n(.*?)\nOutput:\n(.*?)(?=\n--- Part 2 ---|$)/s,
      );
      const part2Match = content.match(
        /--- Part 2 ---\nInput:\n(.*?)\nOutput:\n(.*?)$/s,
      );

      if (part1Match) {
        const [, input, expected] = part1Match.map((s) => s.trim());
        if (part1 && input && expected) {
          test("Part 1 Example", () => {
            expect(String(part1(input))).toBe(expected);
          });
        }
      }

      if (part2Match) {
        const [, input, expected] = part2Match.map((s) => s.trim());
        if (part2 && input && expected) {
          test("Part 2 Example", () => {
            expect(String(part2(input))).toBe(expected);
          });
        }
      }
    }
  });
});
