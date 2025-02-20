function solution(n, stations, w) {
    let cnt = 0;
    let idx = 1;  // 첫 번째 아파트부터 탐색
    let st_idx = 0;
    const cover = 2 * w + 1;  // 기지국 하나가 커버할 수 있는 거리

    while (idx <= n) {
        // 1️⃣ 현재 기지국 범위 내에 있다면, 다음 범위로 이동
        if (st_idx < stations.length && idx >= stations[st_idx] - w) {
            idx = stations[st_idx] + w + 1;  // 기지국이 커버하는 마지막 지점 이후로 이동
            st_idx++;  // 다음 기지국으로 이동
        } 
        // 2️⃣ 전파가 닿지 않는 곳이라면, 새로운 기지국 설치
        else {
            cnt++;
            idx += cover;  // 기지국 하나를 설치하고 다음 범위로 이동
        }
    }

    return cnt;
}
