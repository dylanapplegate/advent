const fs = require('fs');
const path = require('path');

function findSolutionFiles(dir) {
    let solutionFiles = [];
    const files = fs.readdirSync(dir);

    for (const file of files) {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.venv' && file !== '.git') {
                solutionFiles = solutionFiles.concat(findSolutionFiles(filePath));
            }
        } else if (filePath.endsWith(path.join('javascript', 'solution.js'))) {
            solutionFiles.push(filePath);
        }
    }
    return solutionFiles;
}

const solutionPaths = findSolutionFiles(process.cwd());

solutionPaths.forEach(solutionPath => {
    const solutionDir = path.dirname(solutionPath);
    const dayDir = path.dirname(solutionDir);
    const relativePath = path.relative(process.cwd(), solutionPath);

    describe(relativePath, () => {
        const solution = require(solutionPath);
        const part1 = solution.part1;
        const part2 = solution.part2;


        const testDataPath = path.join(dayDir, 'test_data.json');
        if (fs.existsSync(testDataPath)) {
            const testData = JSON.parse(fs.readFileSync(testDataPath, 'utf-8'));

            if (part1 && testData.part1 && testData.part1.length > 0) {
                test('Part 1 JSON', () => {
                    for (const { input, expected } of testData.part1) {
                        expect(part1(input)).toBe(expected);
                    }
                });
            }

            if (part2 && testData.part2 && testData.part2.length > 0) {
                test('Part 2 JSON', () => {
                    for (const { input, expected } of testData.part2) {
                        expect(part2(input)).toBe(expected);
                    }
                });
            }
        }

        const exampleDataPath = path.join(dayDir, 'example_1.txt');
        if (fs.existsSync(exampleDataPath)) {
            const exampleData = fs.readFileSync(exampleDataPath, 'utf-8');
            if (exampleData.includes('---')) {
                const [input, expected] = exampleData.split('---');
                const expectedPart1Match = expected.match(/Part 1: (.*)/);
                const expectedPart1 = expectedPart1Match ? expectedPart1Match[1].trim() : null;

                const expectedPart2Match = expected.match(/Part 2: (.*)/);
                const expectedPart2 = expectedPart2Match ? expectedPart2Match[1].trim() : null;

                if (part1 && expectedPart1) {
                    test('Part 1 Example', () => {
                        expect(String(part1(input.trim()))).toBe(expectedPart1);
                    });
                }

                if (part2 && expectedPart2) {
                    test('Part 2 Example', () => {
                        expect(String(part2(input.trim()))).toBe(expectedPart2);
                    });
                }
            }
        }
    });
});