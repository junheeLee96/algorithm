const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n, m;
let arr;

rl.on("line", (line) => {
  if (!n) {
    [n, m] = line.split(" ").map(Number);
  } else {
    arr = line.split(" ").map(Number);
  }
}).on("close", () => {
  arr.sort((a, b) => a - b);
  let cnt = 0;

  let left = 0;
  let right = n - 1;
  while (left < right) {
    if (arr[left] + arr[right] >= m) {
      right--;
      left++;
      cnt++;
    } else {
      left++;
    }
  }
  console.log(cnt);
});
