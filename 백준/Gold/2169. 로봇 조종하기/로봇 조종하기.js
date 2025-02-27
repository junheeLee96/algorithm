const fs = require('fs');
const input = fs.readFileSync('/dev/stdin', 'utf8').trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const data = input.slice(1).map(line => line.split(' ').map(Number));

// DP 테이블 초기화
const dp = Array.from({ length: n }, () => Array(m).fill(0));
dp[0] = [...data[0]];

// 첫 번째 행을 누적으로 채우기
for (let i = 1; i < m; i++) {
    dp[0][i] += dp[0][i - 1];
}

for (let i = 1; i < n; i++) {
    let tmp1 = Array(m).fill(0); // 왼쪽 > 오른쪽 최대값
    let tmp2 = Array(m).fill(0); // 오른쪽 > 왼쪽 최대값

    for (let j = 0; j < m; j++) {
        if (j === 0) {
            tmp1[j] = data[i][j] + dp[i - 1][j];
            tmp2[m - 1 - j] = data[i][m - 1 - j] + dp[i - 1][m - 1 - j];
            continue;
        }
        tmp1[j] = data[i][j] + Math.max(dp[i - 1][j], tmp1[j - 1]);
        tmp2[m - 1 - j] = data[i][m - 1 - j] + Math.max(dp[i - 1][m - 1 - j], tmp2[m - j]);
    }

    // tmp1과 tmp2 중 최대값을 dp에 갱신
    dp[i] = tmp1.map((val, idx) => Math.max(val, tmp2[idx]));
}

console.log(dp[n - 1][m - 1]);
