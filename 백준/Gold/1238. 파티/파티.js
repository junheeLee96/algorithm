const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n, m, x;
let dist = [];
const INF = Infinity;
let answer = -1;

rl.on("line", (line) => {
  if (!n) {
    [n, m, x] = line.split(" ").map(Number);
    dist = Array.from({ length: n + 1 }, () =>
      Array.from({ length: n + 1 }, () => INF)
    );
  } else {
    let [a, b, c] = line.split(" ").map(Number);
    dist[a][b] = c;
  }
}).on("close", () => {
  for (let i = 1; i <= n; i++) {
    dist[i][i] = 0;
  }
  floyd();
  for (let i = 1; i <= n; i++) {
    answer = Math.max(dist[i][x] + dist[x][i], answer);
  }
  console.log(answer);
});

function floyd() {
  for (let k = 1; k <= n; k++) {
    for (let i = 1; i <= n; i++) {
      for (let j = 1; j <= n; j++) {
        if (dist[i][k] !== INF && dist[k][j] !== INF) {
          dist[i][j] = Math.min(dist[i][j], dist[i][k] + dist[k][j]);
        }
      }
    }
  }
}
