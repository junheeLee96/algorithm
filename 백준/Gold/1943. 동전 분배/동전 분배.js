const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
rl.on("line", (line) => {
    input.push(line);
}).on("close", () => {
    processInput(input.join("\n"));
    process.exit(0);
});

function canDivideCoins(N, coins) {
    let totalSum = coins.reduce((sum, [price, amount]) => sum + price * amount, 0);
    
    if (totalSum % 2 === 1) return 0; // 총합이 홀수면 나눌 수 없음

    let target = totalSum / 2;
    let DP = Array.from({ length: N + 1 }, () => Array(target + 1).fill(false));
    DP[0][0] = true;

    for (let i = 1; i <= N; i++) {
        let [price, amount] = coins[i - 1];

        for (let j = 0; j <= target; j++) {
            if (DP[i - 1][j]) {
                for (let k = 0; k <= amount; k++) {
                    let tempAmount = j + price * k;
                    if (tempAmount <= target) {
                        DP[i][tempAmount] = true;
                    }
                }
            }
        }
    }

    return DP[N][target] ? 1 : 0;
}

function processInput(input) {
    let lines = input.trim().split("\n");
    let index = 0;
    let results = [];

    for (let tc = 0; tc < 3; tc++) { // 3개의 테스트 케이스
        let N = parseInt(lines[index++]);
        let coins = [];

        for (let i = 0; i < N; i++) {
            coins.push(lines[index++].split(" ").map(Number));
        }

        results.push(canDivideCoins(N, coins));
    }

    console.log(results.join("\n"));
}
