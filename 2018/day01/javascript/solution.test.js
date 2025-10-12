const fs = require('fs');
const path = require('path');
const { part1, part2 } = require('./solution');

function readFile(filename) {
    return fs.readFileSync(path.join(__dirname, '..', filename), 'utf-8');
}

describe('Day 1', () => {
    const testData = JSON.parse(readFile('test_data.json'));
    if (testData.part1.length > 0) {
        test('Part 1 JSON', () => {
            for (const { input, expected } of testData.part1) {
                expect(part1(input)).toBe(expected);
            }
        });
    }

    if (testData.part2.length > 0) {
        test('Part 2 JSON', () => {
            for (const { input, expected } of testData.part2) {
                expect(part2(input)).toBe(expected);
            }
        });
    }

    const exampleData = readFile('example_1.txt');
    if (exampleData.includes('---')) {
        const [input, expected] = exampleData.split('---');
        const expectedPart1 = expected.match(/Part 1: (.*)/)[1].trim();
        const expectedPart2 = expected.match(/Part 2: (.*)/)[1].trim();

        if (expectedPart1) {
            test('Part 1 Example', () => {
                expect(String(part1(input.trim()))).toBe(expectedPart1);
            });
        }

        if (expectedPart2) {
            test('Part 2 Example', () => {
                expect(String(part2(input.trim()))).toBe(expectedPart2);
            });
        }
    }
});