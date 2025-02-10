function solution(n, wires) {
    let answer = Infinity;

    // 유니온 파인드: 부모 찾기
    const getParent = (parent, x) => {
        if (parent[x] === x) return x;
        return parent[x] = getParent(parent, parent[x]); // 경로 압축
    };

    // 유니온 파인드: 두 집합 합치기
    const unionParent = (parent, x, y) => {
        let a = getParent(parent, x);
        let b = getParent(parent, y);
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    };

    // 모든 간선 하나씩 제거
    for (let i = 0; i < n - 1; i++) {
        let parent = Array.from({ length: n + 1 }, (_, idx) => idx); // 부모 초기화

        // 현재 간선을 제외한 나머지 간선들 처리
        for (let j = 0; j < n - 1; j++) {
            if (i === j) continue;
            unionParent(parent, wires[j][0], wires[j][1]);
        }

        // 각 그룹의 크기 계산
        let groupSize = Array(n + 1).fill(0); // 그룹별 크기 저장
        for (let k = 1; k <= n; k++) {
            let root = getParent(parent, k);
            groupSize[root]++;
        }

        // 두 그룹의 크기 차이 계산
        let sizes = Object.values(groupSize).filter(size => size > 0);
        let diff = Math.abs(sizes[0] - sizes[1]);
        answer = Math.min(answer, diff);
    }

    return answer;
}
