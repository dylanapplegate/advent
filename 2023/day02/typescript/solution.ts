function getCubeMaxes(game: string): [number, Record<string, number>] {
  const cubeCount: Record<string, number> = {};
  const [gameString, contentString] = game
    .trim()
    .split(":")
    .map((s) => s.trim());
  const turns = contentString.split(";").map((s) => s.trim());
  const gameId = Number(gameString.split(" ")[1]);

  for (const turn of turns) {
    turn
      .split(",")
      .map((cube) => {
        const [count, color] = cube.trim().split(" ");
        return [color, Number(count)];
      })
      .forEach(([color, count]) => {
        cubeCount[color as string] = Math.max(cubeCount[color as string] ?? 0, count as number);
      });
  }

  return [gameId, cubeCount];
}

function formatData(input: string): [number, Record<string, number>][] {
  const gameRows = input.trim().split("\n");
  const gameDictionaries = gameRows.map((row) => getCubeMaxes(row));
  return gameDictionaries;
}

function isPossible(cubeCount: Record<string, number>): boolean {
  const onHand: Record<string, number> = { red: 12, green: 13, blue: 14 };

  for (const [color, count] of Object.entries(onHand)) {
    if (color in cubeCount && count < cubeCount[color]) {
      return false;
    }
  }
  return true;
}

export function part1(input: string): number {
  const games = formatData(input);
  const validGames = games
    .filter(([gameId, game]) => isPossible(game))
    .map(([gameId, game]) => gameId)
    .reduce((a, v) => a + v);
  return validGames;
}

function powerOfCubes(cubeCount: Record<string, number>): number {
  return ["red", "blue", "green"].reduce((acc, key) => acc * (cubeCount[key] ?? 0), 1);
}

export function part2(input: string): number {
  return formatData(input)
    .map(([, game]) => powerOfCubes(game))
    .reduce((acc, gameId) => acc + gameId);
}
