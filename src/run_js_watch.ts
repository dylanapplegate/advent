import { spawn } from 'child_process';
import fs from 'fs';
import path from 'path';
import chokidar from 'chokidar';

const [, , year, day] = process.argv;

if (!year || !day) {
  console.error('Usage: node run_js_watch.js <YEAR> <DAY>');
  process.exit(1);
}

const dayPadded = `day${day.padStart(2, '0')}`;
const solutionPath = path.join(
  'src',
  year,
  dayPadded,
  'typescript',
  'solution.ts',
);

if (!fs.existsSync(solutionPath)) {
  console.error(`Error: Solution path not found at ${solutionPath}`);
  process.exit(1);
}

function runTestsAndSolution() {
  const testPattern = `src/${year}/${dayPadded}`;
  const jest = spawn('jest', ['--testNamePattern', testPattern], {
    stdio: 'inherit',
  });

  jest.on('close', (code) => {
    if (code !== 0) {
      console.error('Tests Failed. Skipping final solution run.');
      return;
    }

    console.log('All tests passed!');

    // Clear the module cache for the solution file to pick up changes
    delete require.cache[require.resolve(path.resolve(solutionPath))];
    const solution = require(path.resolve(solutionPath));
    const inputFilePath = path.join('src', year, dayPadded, 'input.txt');
    const inputData = fs.readFileSync(inputFilePath, 'utf-8');
    const { part1, part2 } = solution;

    const part1Result = part1(inputData);
    const part2Result = part2(inputData);

    console.log(`Part 1: ${part1Result}`);
    console.log(`Part 2: ${part2Result}`);
  });
}

runTestsAndSolution();

const watcher = chokidar.watch(solutionPath);

watcher.on('change', () => {
  process.stdout.write('\x1Bc');
  console.log('Solution file changed. Re-running tests...');
  runTestsAndSolution();
});
