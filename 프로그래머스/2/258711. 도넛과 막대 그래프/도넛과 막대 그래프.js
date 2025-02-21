function defaultdict(factory) {
    return new Proxy({}, {
        get: (obj, prop) => prop in obj ? obj[prop] : (obj[prop] = factory())
    });
}

function solution(edges) {
    // 생성된 노드를 판단
    const n = edges.length;
    const nodes = new Set();
    // 나가는 애
    let conn = defaultdict(() => []);
    // 들어오는 애 
    let reverse_conn = defaultdict(() => []);
    for (let [a, b] of edges) {
        nodes.add(a);
        nodes.add(b);
        conn[a].push(b); // a -> b
        reverse_conn[b].push(a); // b <- a
    }

    function get_generated_node() {
        for (let node of nodes) {
            // 들어오는 애가 있다면 컨티뉴
            if (reverse_conn[node].length > 0) continue;
            // 나가는 애가 2개 미만이라면 컨티뉴
            else if (conn[node].length < 2) continue;
            return node;
        }
    }

    // 생성된 정점
    let gn = get_generated_node();
    
    let graph_node = [...conn[gn]];
    let answer = [gn, 0, 0, 0];
    
    // 스택 기반으로 DFS 탐색
    function search(node) {
        let stack = [node];
        let visit = new Set();

        while (stack.length > 0) {
            let curr = stack.pop();

            if (!conn[curr] || conn[curr].length === 0) {
                return "막대";
            }

            if (visit.has(curr)) {
                return "도넛";
            }

            // 나한테서 나가는 애가 2개 이상이라면 "8자"
            if (conn[curr].length >= 2) {
                return "8자";
            }

            // 나에게로 들어오는 애(생성된 노드에서 뻗어나온 화살표는 제외해야 함)
            if (reverse_conn[curr]) {
                let in_arrow = [...reverse_conn[curr]].filter(v => v !== gn);
                if (in_arrow.length >= 2) {
                    return "8자";
                }
            }

            visit.add(curr);
            stack.push(conn[curr][0]);
        }

        return "막대";  // 최종적으로 "막대"를 리턴
    }

    for (let g_node of graph_node) {
        let result = search(g_node);
        if (result === '막대') {
            answer[2] += 1;
        } else if (result === '도넛') {
            answer[1] += 1;
        } else if (result === '8자') {
            answer[3] += 1;
        }
    }

    return answer;
}
