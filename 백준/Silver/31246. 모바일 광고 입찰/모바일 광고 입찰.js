const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on("line", (line) => {
  input.push(line);
}).on("close", () => {
  const [N, K] = input[0].split(" ").map(Number);
  let X = [];

  for (let i = 1; i <= N; i++) {
    const [A, B] = input[i].split(" ").map(Number);
    X.push(B - A);
  }

  X.sort((a, b) => a - b); // 오름차순 정렬

  console.log(X[K - 1] < 0 ? 0 : X[K - 1]);
});
