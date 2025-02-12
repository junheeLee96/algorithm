function solution(user_id, banned_id) {
    let answer = new Set();  // 중복 제거를 위해 Set 사용
    let matched = [];  // 각 banned_id에 매칭될 수 있는 user_id 리스트

    // 1. banned_id와 매칭 가능한 user_id 찾기
    for (let ban of banned_id) {
        let regex = new RegExp(`^${ban.replace(/\*/g, ".")}$`); // 정규식 변환
        matched.push(user_id.filter(user => regex.test(user))); // 매칭되는 유저 저장
    }
    console.log(matched)
    // 2. 백트래킹으로 가능한 조합 찾기
    function dfs(idx, used) {
        if (idx === banned_id.length) {
            answer.add([...used].sort().join(","));  // 정렬해서 중복 방지
            return;
        }
        
        for (let user of matched[idx]) {
            if (!used.has(user)) {  // 이미 사용된 user인지 체크
                used.add(user);
                dfs(idx + 1, used);
                used.delete(user);
            }
        }
    }

    dfs(0, new Set());  // DFS 탐색 시작

    return answer.size;
}
