function timeToMin(timeValue) {
    return Math.floor(timeValue / 100) * 60 + (timeValue % 100);
}

function solution(schedules, timelogs, startday) {
    let answer = 0;
    startday -= 1;  // startday를 0-based로 변환

    for (let i = 0; i < schedules.length; i++) {
        let stand = timeToMin(schedules[i]) + 10;
        let isOnTime = true;
        let day = startday;

        for (let j = 0; j < 7; j++) {
            let nowday = (day + j) % 7;
            if (nowday === 5 || nowday === 6) continue; // 토(5), 일(6) 체크

            let cur = timeToMin(timelogs[i][j]);
            if (cur > stand) {
                isOnTime = false;
                break;
            }
        }

        if (isOnTime) answer++;
    }
    return answer;
}
