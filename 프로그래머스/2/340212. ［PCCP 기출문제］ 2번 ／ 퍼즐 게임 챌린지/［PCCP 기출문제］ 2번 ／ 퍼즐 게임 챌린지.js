function solution(diffs, times, limit) {
//     time_prev 이전 퍼즐의 소요 시간
//     time_cur 현재 퍼즐의 소요 시간
//     diff 현재 퍼즐의 난이도
//     level 숙련도
    var answer = 100_000;
    let start = 1
    let end = 100_000;
    const n = diffs.length;
    while(start <= end){
        const mid = Math.floor((start + end) / 2);
        let temp = 0;
        for(let i=0; i <n; i++){
            if(mid >= diffs[i]){
                temp += times[i]
            }else{
                let t = ((times[i] + times[i-1]) * (diffs[i] - mid )) + times[i];
                temp += t;
            }
        }
        if(temp > limit){
            start = mid + 1
        }else{
            end = mid - 1
        }
    }
    return start;
}