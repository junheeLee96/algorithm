const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n;
let arr;
let x;
rl.on("line", (line) => {
  if (!n) {
    n = parseInt(line);
  } else if (!arr) {
    arr = line.split(" ").map(Number);
  } else {
    x = parseInt(line);
  }
}).on("close", () => {
  arr.sort((a, b) => a - b);
  let left = 0;
  let right = n - 1;
  let cnt = 0;
  while (left < right) {
    const num = arr[left] + arr[right];
    if (num < x) {
      left++;
    } else if (num > x) {
      right--;
    } else if (num === x) {
      cnt++;
      left++;
    }
  }
  console.log(cnt);
});
