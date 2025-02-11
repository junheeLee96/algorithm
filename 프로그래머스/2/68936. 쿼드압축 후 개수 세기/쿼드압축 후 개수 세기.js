function solution(arr) {
    const n = arr.length;
    const answer = [0, 0];

    function dfs(x, y, length) {
        const current = arr[x][y];
        
        // 1. 현재 구역이 같은 숫자인지 확인
        for (let i = x; i < x + length; i++) {
            for (let j = y; j < y + length; j++) { // ✅ j는 y에서 시작해야 함
                if (arr[i][j] !== current) { // 다른 숫자가 하나라도 나오면 분할
                    const half = length / 2;
                    dfs(x, y, half);
                    dfs(x + half, y, half);
                    dfs(x, y + half, half);
                    dfs(x + half, y + half, half);
                    return; // ✅ 재귀 호출 후에는 return 필요
                }
            }
        }

        // 2. 모든 숫자가 같다면 해당 숫자 개수 증가
        answer[current] += 1;
    }

    dfs(0, 0, n);
    return answer;
}
