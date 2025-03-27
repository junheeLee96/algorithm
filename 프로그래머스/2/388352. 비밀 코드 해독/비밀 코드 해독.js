function solution(n, q, ans) {
    let answer = 0;
    const arr = Array.from({length: n}, (_, i) => i + 1); // 1부터 n까지 배열 생성
    
    let comb = getComb(arr, 5); // 5개씩 조합 생성
    
    for (let cur of comb) {
        let isValid = true; // 각 조합이 조건을 만족하는지 체크
        
        for (let i = 0; i < q.length; i++) {
            // q[i]는 각 조건을 나타내는 배열이고, ans[i]는 그에 맞는 답을 나타냄
            let intersectionCount = cur.filter(val => q[i].includes(val)).length;
            
            // 조건을 만족하지 않으면 더 이상 검사하지 않고 넘어감
            if (intersectionCount !== ans[i]) {
                isValid = false;
                break;
            }
        }

        // 모든 조건을 만족하는 조합이면 카운트 증가
        if (isValid) {
            answer++;
        }
    }

    return answer;
}

function getComb(arr, mx) {
    let result = [];
    
    function dfs(cur, idx) {
        if (cur.length === mx) {
            result.push([...cur]); // 완성된 조합을 result에 추가
            return;
        }
        for (let i = idx; i < arr.length; i++) {
            cur.push(arr[i]);
            dfs(cur, i + 1); // 다음 인덱스를 선택하도록
            cur.pop(); // 백트래킹 (이전 상태로 되돌리기)
        }
    }
    
    dfs([], 0); // 빈 배열에서 시작
    return result;
}
