function solution(board) {
    var answer = -1;
    
    let q = [];
    let n = board.length;
    let m = board[0].length;
    let end = []
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (board[i][j] === 'R') {
                q.push([i, j, 0]);  // 출발점 추가
            }
            if (board[i][j] === 'G') {
                end = [i, j];  // 목표점
            }
        }
    }

    let visit = Array.from({ length: n }, () => Array(m).fill(false));
    visit[q[0][0]][q[0][1]] = true;

    const dx = [0, 0, -1, 1];
    const dy = [-1, 1, 0, 0];

    while (q.length > 0) {
        const [x, y, cnt] = q.shift(); 

        for (let i = 0; i < 4; i++) {
            let nx = x + dx[i];
            let ny = y + dy[i];

            // 직선으로 이동
            while (0 <= nx && nx < n && 0 <= ny && ny < m && board[nx][ny] !== 'D') {
                nx += dx[i];
                ny += dy[i];
            }

            // 벽을 넘지 않도록 수정
            nx -= dx[i];
            ny -= dy[i];

            // 이미 방문한 곳이라면 넘어감
            if (visit[nx][ny] === true) continue;

            // 목표에 도달했다면
            if (board[nx][ny] === 'G') {
                return cnt + 1;
            }

            // 방문 처리 후 큐에 넣기
            visit[nx][ny] = true;
            q.push([nx, ny, cnt + 1]);
        }
    }
    
    return answer;
}
