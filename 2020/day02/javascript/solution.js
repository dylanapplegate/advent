function extractData(line) {
  const [policyPart, passwordPart] = line.trim().split(":");
  const password = passwordPart.trim();
  const [countRange, letter] = policyPart.trim().split(/\s+/g);
  const [minPart, maxPart] = countRange.trim().split("-");
  const minCount = Number(minPart);
  const maxCount = Number(maxPart);

  return [minCount, maxCount, letter, password];
}

function formatData(input) {
  return input
    .trim()
    .split("\n")
    .map((line) => extractData(line));
}

function isValid(policy) {
  const [minCount, maxCount, char, password] = policy;
  const charCount = password.split(char).length - 1;
  return minCount <= charCount && charCount <= maxCount;
}
function isValid2(policy) {
  const [position1, position2, char, password] = policy;
  const position1Valid = password[position1 - 1] === char;
  const position2Valid = password[position2 - 1] === char;

  return (
    (position1Valid && !position2Valid) || (position2Valid && !position1Valid)
  );
}

function part1(input) {
  const policiesAndPasswords = formatData(input);
  validPasswords = policiesAndPasswords.filter((policy) => isValid(policy));
  return validPasswords.length;
}

function part2(input) {
  const policiesAndPasswords = formatData(input);
  validPasswords = policiesAndPasswords.filter((policy) => isValid2(policy));
  return validPasswords.length;
}

module.exports = { part1, part2 };
