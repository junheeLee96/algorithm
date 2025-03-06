const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let n;
let arr = [];
let teacher = [];
let student = [];
let empty = [];
let temp = 0;

rl.on('line', (line) => {
    if (!n) {
        n = parseInt(line);
    } else {
        let a = line.split(' ');
        for (let i = 0; i < n; i++) {
            if (a[i] === 'X') {
                empty.push([temp, i]);
            } else if (a[i] === 'T') {
                teacher.push([temp, i]);
            } else if (a[i] === 'S') {
                student.push([temp, i]);
            }
        }
        arr.push(a);
        temp++;
    }
}).on('close', () => {
    let combi = getComb(empty, empty.length); // ✅ n 대신 empty.length 사용

    for (let comb of combi) {
        const temp = getAnswer(comb, arr);
        if (temp) {
            console.log('YES');
            return;
        }
    }
    console.log('NO');
});

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];

function getDir(x, y, i) {
    let nx = x + dx[i];
    let ny = y + dy[i];
    return [nx, ny];
}

function getAnswer(comb, origin) {
    const arr = origin.map(row => [...row]); // ✅ 깊은 복사 수정

    for (let [x, y] of comb) {
        arr[x][y] = 'W';
    }

    for (let [sx, sy] of teacher) { // ✅ 변수명 변경 (원래 좌표 유지)
        for (let i = 0; i < 4; i++) {
            let [x, y] = [sx, sy];
            while (0 <= x && x < n && 0 <= y && y < n) {
                [x, y] = getDir(x, y, i);
                if (x < 0 || x >= n || y < 0 || y >= n) break; // ✅ 배열 범위 초과 방지
                if (arr[x][y] === 'W') break;
                if (arr[x][y] === 'S') return false;
            }
        }
    }

    return true;
}

function getComb(array, size) { // ✅ n 대신 size
    let maxLen = 3;
    let result = [];

    function dfs(temp, idx) {
        if (temp.length === maxLen) {
            result.push([...temp]);
            return;
        }

        for (let i = idx; i < size; i++) { // ✅ n 대신 size
            temp.push(array[i]);
            dfs(temp, i + 1);
            temp.pop();
        }
    }

    dfs([], 0);
    return result;
}
