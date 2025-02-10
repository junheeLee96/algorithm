const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n, m, r;
let arr = [];
let dist = [];
let score = [0];
let temp = 0;

const INF = Infinity;

rl.on("line", (line) => {
  if (!n) {
    [n, m, r] = line.split(" ").map(Number);
    arr = Array.from({ length: n + 1 }, () => []);
    dist = Array.from({ length: n + 1 }, () =>
      Array.from({ length: n + 1 }, () => INF)
    );
    temp++;
  } else if (temp === 1) {
    temp++;
    score = line.split(" ").map(Number);
  } else {
    let [a, b, c] = line.split(" ").map(Number);
    dist[a][b] = c;
    dist[b][a] = c;
    // arr[a].push([b, c]);
    // arr[b].push([a, c]);
  }
}).on("close", () => {
  for (let i = 1; i <= n; i++) {
    dist[i][i] = 0;
  }

  floyd();
  let answer = -1;

  for (let i = 1; i <= n; i++) {
    let temp = 0;
    for (let j = 1; j <= n; j++) {
      if (dist[i][j] > m) continue;
      temp += score[j - 1];
    }
    answer = Math.max(temp, answer);
  }
  console.log(answer);
});

function floyd() {
  for (let k = 1; k <= n; k++) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        if (dist[i][k] !== INF && dist[k][j] != INF) {
          dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
  }
}