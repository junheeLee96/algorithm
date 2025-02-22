const dx = [1, 0, 0, -1];  // "d", "l", "r", "u"
const dy = [0, -1, 1, 0];
const dir = ["d", "l", "r", "u"];  // 사전순 정렬 고려

function solution(n, m, x, y, r, c, k) {
    let minDist = Math.abs(x - r) + Math.abs(y - c);
    
    // 도달 불가능한 경우
    if (minDist > k || (k - minDist) % 2 !== 0) return "impossible";
    
    let result = "";

    function dfs(cx, cy, path, steps) {
        if (result) return;  // 이미 정답 찾으면 더 이상 탐색X
        if (steps === k) {
            if (cx === r && cy === c) result = path;
            return;
        }
        
        for (let i = 0; i < 4; i++) {
            let nx = cx + dx[i];
            let ny = cy + dy[i];
            let remainingDist = Math.abs(nx - r) + Math.abs(ny - c);

            if (1 <= nx && nx <= n && 1 <= ny && ny <= m && remainingDist <= k - steps - 1) {
                dfs(nx, ny, path + dir[i], steps + 1);
            }
        }
    }

    dfs(x, y, "", 0);
    
    return result || "impossible";
}
