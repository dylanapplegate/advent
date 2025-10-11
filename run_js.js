
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const [,, year, day] = process.argv;

if (!year || !day) {
    console.error('Usage: node run_js.js <YEAR> <DAY>');
    process.exit(1);
}

const dayPadded = `day${day.padStart(2, '0')}`;
const solutionPath = path.join(year, dayPadded, 'javascript');

if (!fs.existsSync(solutionPath)) {
    console.error(`Error: Solution path not found at ${solutionPath}`);
    process.exit(1);
}

const jest = spawn('jest', [solutionPath], { stdio: 'inherit' });

jest.on('close', (code) => {
    if (code !== 0) {
        console.error('Tests Failed. Skipping final solution run.');
        process.exit(1);
    }

    console.log('All tests passed!');

    const inputFilePath = path.join(year, dayPadded, 'input.txt');
    const inputData = fs.readFileSync(inputFilePath, 'utf-8');

    const { part1, part2 } = require(path.resolve(solutionPath, 'solution.js'));

    const part1Result = part1(inputData);
    const part2Result = part2(inputData);

    console.log(`Part 1: ${part1Result}`);
    console.log(`Part 2: ${part2Result}`);
});
