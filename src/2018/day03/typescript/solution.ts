function getFabricTuple(line: string): number[] {
  return line.match(/\d+/g).map(Number);
}

function formatData(input: string): number[][] {
  return input.trim().split('\n').map(getFabricTuple);
}
function getClaimsMapKey(y: number, x: number): string {
  return `${y}:${x}`;
}

function getClaimsMap(claims: number[][]): Map<string, number[]> {
  const claimsMap = new Map();

  for (const [claimId, oy, ox, h, w] of claims) {
    for (let ny = oy; ny < oy + h; ny++) {
      for (let nx = ox; nx < ox + w; nx++) {
        const key = getClaimsMapKey(ny, nx);
        const value = claimsMap.get(key) ?? [];
        value.push(claimId);
        claimsMap.set(key, value);
      }
    }
  }
  return claimsMap;
}

export function part1(input: string): number | string | undefined {
  const claims = formatData(input);
  const claimsMap = getClaimsMap(claims);

  return [...claimsMap.values()].filter((claimIds) => claimIds.length > 1)
    .length;
}

export function part2(input: string): number | string | undefined {
  const claims = formatData(input);
  const claimsMap = getClaimsMap(claims);

  const possibleClaims: Set<number> = new Set(claims.map((claim) => claim[0]));
  const invalidClaims = new Set();

  claimsMap.forEach((claimIds) => {
    if (claimIds.length === 1) {
      return;
    }
    claimIds.forEach((claimId) => invalidClaims.add(claimId));
  });

  const validClaims = possibleClaims.difference(invalidClaims);
  return [...validClaims][0];
}
