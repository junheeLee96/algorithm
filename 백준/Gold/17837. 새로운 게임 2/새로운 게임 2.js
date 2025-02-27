const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n, k;
let arr = [];
let temp = 0;
let temp2 = 0;

const dx = [0, 0, -1, 1]; // 오 왼 위 아래
const dy = [1, -1, 0, 0];
let maps = [];
let info = [];

rl.on("line", (line) => {
    if (!n) {
        [n, k] = line.split(" ").map(Number);
        maps = Array.from({ length: n }, () => Array.from({ length: n }, () => []));
    } else if (temp < n) {
        arr.push(line.split(" ").map(Number));
        temp++;
    } else {
        let [x, y, dir] = line.split(" ").map(Number);
        info.push([x - 1, y - 1, dir - 1]);
        maps[x - 1][y - 1].push(temp2);
        temp2++;
    }
}).on("close", () => {
    console.log(solution());
});

function solution() {
    let cnt = 0;

    while (cnt <= 1000) {
        cnt++;

        for (let i = 0; i < k; i++) {
            let [x, y, dir] = info[i];

            let nx = x + dx[dir];
            let ny = y + dy[dir];

            // 범위를 벗어나거나 파란색(2)을 만나면 방향 반전
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || arr[nx][ny] === 2) {
                dir = dir % 2 === 0 ? dir + 1 : dir - 1;
                nx = x + dx[dir];
                ny = y + dy[dir];

                info[i][2] = dir; // 방향 업데이트

                // 반대 방향도 이동 불가하면 제자리 유지
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || arr[nx][ny] === 2) {
                    continue;
                }
            }

            // 현재 위치에서 이동할 말들 찾기
            const idx = maps[x][y].indexOf(i);
            const children = maps[x][y].splice(idx);

            // 이동하는 말들의 좌표 갱신
            for (let child of children) {
                info[child][0] = nx;
                info[child][1] = ny;
            }

            // 빨간색(1)이면 순서 뒤집기
            if (arr[nx][ny] === 1) {
                children.reverse();
            }

            // 새로운 위치에 말 추가
            maps[nx][ny].push(...children);

            // 게임 종료 조건: 한 칸에 말이 4개 이상 쌓이면 종료
            if (maps[nx][ny].length >= 4) {
                return cnt;
            }
        }
    }

    return -1;
}
