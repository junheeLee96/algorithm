const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let a, b;

rl.on("line", (line) => {
    [a, b] = line.split(' ').map(Number);

}).on("close", () => {
    console.log(a+b)
});
