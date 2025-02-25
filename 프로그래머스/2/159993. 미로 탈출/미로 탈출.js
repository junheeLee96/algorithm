function solution(maps) {
    let n = maps.length, m = maps[0].length;
    let s, l, e;

    // S, L, E 좌표 찾기
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (maps[i][j] === 'S') s = [i, j];
            else if (maps[i][j] === 'L') l = [i, j];
            else if (maps[i][j] === 'E') e = [i, j];
        }
    }

    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];

    // BFS 함수
    function bfs(startX, startY, target) {
        let visit = Array.from({ length: n }, () => Array(m).fill(-1));
        let q = [[startX, startY]];
        visit[startX][startY] = 0;

        while (q.length > 0) {
            const [x, y] = q.shift();  // ✅ BFS는 shift() 사용

            for (let i = 0; i < 4; i++) {
                let nx = x + dx[i];
                let ny = y + dy[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] !== 'X' && visit[nx][ny] === -1) {
                    visit[nx][ny] = visit[x][y] + 1;
                    q.push([nx, ny]);

                    if (maps[nx][ny] === target) return visit[nx][ny];  // 목표 도달 시 반환
                }
            }
        }
        return -1;
    }

    // S → L 거리
    let toLever = bfs(s[0], s[1], 'L');
    if (toLever === -1) return -1;

    // L → E 거리
    let toExit = bfs(l[0], l[1], 'E');
    if (toExit === -1) return -1;

    return toLever + toExit;
}
