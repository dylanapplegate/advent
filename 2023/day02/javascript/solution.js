function getCubeMaxes(game) {
  const cubeCount = {};
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
        return [color, count];
      })
      .forEach(([color, count]) => {
        cubeCount[color] = Math.max(cubeCount[color] ?? 0, count);
      });
  }

  return [gameId, cubeCount];
}

function formatData(input) {
  const gameRows = input.trim().split("\n");
  const gameDictionaries = gameRows.map((row) => getCubeMaxes(row));
  return gameDictionaries;
}

function isPossible(cubeCount) {
  const onHand = { red: 12, green: 13, blue: 14 };

  for (const [color, count] of Object.entries(onHand)) {
    if (color in cubeCount && count < cubeCount[color]) {
      return false;
    }
  }
  return true;
}

function part1(input) {
  const games = formatData(input);
  const validGames = games
    .filter(([gameId, game]) => isPossible(game))
    .map(([gameId, game]) => gameId)
    .reduce((a, v) => a + v);
  return validGames;
}

function powerOfCubes(cubeCount) {
  return ["red", "blue", "green"].reduce((acc, key) => acc * cubeCount[key], 1);
}

function part2(input) {
  return formatData(input)
    .map(([, game]) => powerOfCubes(game))
    .reduce((acc, gameId) => acc + gameId);
}

module.exports = { part1, part2 };
