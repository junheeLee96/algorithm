function find(parent, x) {
    if (parent[x] !== x) parent[x] = find(parent, parent[x]);
    return parent[x];
}

function union(parent, a, b) {
    const rootA = find(parent, a);
    const rootB = find(parent, b);
    if (rootA !== rootB) parent[rootB] = rootA;
}

function solution(n, costs) {
    costs.sort((a, b) => a[2] - b[2]); // 비용 기준 정렬
    const parent = Array.from({ length: n }, (_, i) => i);
    let totalCost = 0, count = 0;

    for (const [a, b, cost] of costs) {
        if (find(parent, a) !== find(parent, b)) {
            union(parent, a, b);
            totalCost += cost;
            count++;
            if (count === n - 1) break; // 모든 섬이 연결되면 종료
        }
    }

    return totalCost;
}
