const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let n, k;
let board = [];
let maps = [];
let pieces = [];

const dx = [0, 0, -1, 1]; // 우, 좌, 상, 하
const dy = [1, -1, 0, 0];

rl.on("line", (line) => {
    if (!n) {
        [n, k] = line.split(" ").map(Number);
        board = [];
        maps = Array.from({ length: n }, () => Array.from({ length: n }, () => []));
    } else if (board.length < n) {
        board.push(line.split(" ").map(Number));
    } else {
        let [x, y, dir] = line.split(" ").map(Number);
        pieces.push([x - 1, y - 1, dir - 1]);
        maps[x - 1][y - 1].push(pieces.length - 1);
    }
}).on("close", () => {
    console.log(solution());
});

function solution() {
    let turn = 0;

    while (turn <= 1000) {
        turn++;

        for (let i = 0; i < k; i++) {
            let [x, y, dir] = pieces[i];

            let nx = x + dx[dir];
            let ny = y + dy[dir];

            // 범위를 벗어나거나 파란색일 경우 방향 반전
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] === 2) {
                dir = dir % 2 === 0 ? dir + 1 : dir - 1;
                nx = x + dx[dir];
                ny = y + dy[dir];

                pieces[i][2] = dir;

                // 반대 방향 이동도 파란색이거나 범위를 벗어나면 제자리 유지
                if (nx < 0 || nx >= n || ny < 0 || ny >= n || board[nx][ny] === 2) {
                    continue;
                }
            }

            // 현재 위치에서 말들 이동
            let idx = maps[x][y].indexOf(i);
            let movingPieces = maps[x][y].splice(idx);

            // 말들의 위치 업데이트
            for (let piece of movingPieces) {
                pieces[piece][0] = nx;
                pieces[piece][1] = ny;
            }

            // 빨간색이면 순서 뒤집음
            if (board[nx][ny] === 1) {
                movingPieces.reverse();
            }

            maps[nx][ny] = [...maps[nx][ny], ...movingPieces];

            // 한 칸에 말이 4개 이상이면 종료
            if (maps[nx][ny].length >= 4) {
                return turn;
            }
        }
    }

    return -1;
}
