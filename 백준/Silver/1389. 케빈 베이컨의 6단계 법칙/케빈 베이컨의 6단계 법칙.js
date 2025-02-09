const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let arr = [];
let n, m;
let dist;
const INF = Infinity;

rl.on("line", (line) => {
  if (!n) {
    const [a, b] = line.split(" ").map(Number);
    n = a;
    m = b;
    arr = Array.from({ length: n + 1 }, () => []);
    dist = Array.from({ length: n + 1 }, () =>
      Array.from({ length: n + 1 }, () => INF)
    );
  } else {
    const [a, b] = line.split(" ").map(Number);
    arr[a].push(b);
    arr[b].push(a);
    dist[a][b] = 1;
    dist[b][a] = 1;
  }
}).on("close", () => {
  floyd();
  let minKevinBacon = INF;
  let result = -1;

  // 케빈 베이컨 수가 가장 작은 사람을 찾기
  for (let i = 1; i <= n; i++) {
    let kevinBacon = 0;
    for (let j = 1; j <= n; j++) {
      if (dist[i][j] === INF) continue;
      kevinBacon += dist[i][j];
    }
    if (kevinBacon < minKevinBacon) {
      minKevinBacon = kevinBacon;
      result = i;
    }
  }

  console.log(result);
});

function floyd() {
  // 자기 자신과의 거리는 0
  for (let i = 1; i <= n; i++) {
    dist[i][i] = 0;
  }

  // 플로이드 와샬 알고리즘
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
