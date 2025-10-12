
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python scaffold.py <YEAR> <DAY>")
        sys.exit(1)

    year = sys.argv[1]
    day = sys.argv[2]
    day_padded = f"day{day.zfill(2)}"

    base_dir = os.path.join(year, day_padded)
    py_dir = os.path.join(base_dir, "python")
    js_dir = os.path.join(base_dir, "javascript")

    # Create directories
    os.makedirs(py_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)

    # Create empty input.txt
    with open(os.path.join(base_dir, "input.txt"), "w") as f:
        pass

    # Create example_1.txt
    with open(os.path.join(base_dir, "example_1.txt"), "w") as f:
        f.write("""
---
Part 1: 
Part 2: 
""")

    # Create test_data.json
    with open(os.path.join(base_dir, "test_data.json"), "w") as f:
        f.write("""
{
  "part1": [],
  "part2": []
}
""")

    # Python solution template
    py_solution_template = """

def part1(input_data):
    pass

def part2(input_data):
    pass
"""
    with open(os.path.join(py_dir, "solution.py"), "w") as f:
        f.write(py_solution_template.strip())



    # JS solution template
    js_solution_template = """

function part1(input) {
  return undefined;
}

function part2(input) {
  return undefined;
}

module.exports = { part1, part2 };
"""
    with open(os.path.join(js_dir, "solution.js"), "w") as f:
        f.write(js_solution_template.strip())

    # JS test template
    js_test_template = """

const fs = require('fs');
const path = require('path');
const { part1, part2 } = require('./solution');

function readFile(filename) {
    return fs.readFileSync(path.join(__dirname, '..', filename), 'utf-8');
}

describe('Day NN', () => {
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
"""
    with open(os.path.join(js_dir, "solution.test.js"), "w") as f:
        f.write(js_test_template.replace("Day NN", f"Day {day}").strip())
    
    print(f"Scaffolding for Year {year}, Day {day} created successfully.")

if __name__ == "__main__":
    main()
