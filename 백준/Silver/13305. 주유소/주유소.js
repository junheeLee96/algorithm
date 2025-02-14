const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let n;
let km;
let price;

rl.on("line", (line) => {
  if (!n) {
    n = parseInt(line);
  } else if (!km) {
    km = line.split(" ").map(Number);
  } else if (!price) {
    price = line.split(" ").map(Number);
  }
}).on("close", () => {
  let minPrice = price[0];
  let total = 0;
  for (let i = 0; i < n - 1; i++) {
    if (minPrice > price[i]) {
      minPrice = price[i];
    }
    total += minPrice * km[i];
  }
  console.log(total);
});
