function solution(points, routes) {
    var answer = 0;
    let time = []; // 시간에 따른 좌표별 로봇 수 기록
    let map = new Map();

    // 점을 map에 저장
    for (let i = 0; i < points.length; i++) {
        map.set(i + 1, [points[i][0], points[i][1]]);
    }
    
    function getAnswer(route) {
        let cnt = 0; // 시간 단위
        let last = [0, 0]; // 마지막 도달 좌표

        // 각 로봇의 경로 계산
        for (let i = 0; i < route.length - 1; i++) {
            let [startX, startY] = map.get(route[i]);
            let [destX, destY] = map.get(route[i + 1]);

            // 목표 위치까지 이동
            while (startX !== destX || startY !== destY) {
                if (!time[cnt]) time[cnt] = {}; // 시간대마다 기록 초기화
                if (!time[cnt][startX]) time[cnt][startX] = {}; // 좌표별 기록 초기화
                if (!time[cnt][startX][startY]) time[cnt][startX][startY] = 0; // 로봇 수 초기화

                time[cnt][startX][startY] += 1; // 해당 좌표에 로봇이 도달

                // 충돌 체크: 한 위치에 로봇이 두 대 이상 있을 경우
                if (time[cnt][startX][startY] === 2) {
                    answer++;
                }

                // 좌표 이동
                if (startX < destX) startX++;
                else if (startX > destX) startX--;
                else if (startY < destY) startY++;
                else if (startY > destY) startY--;

                cnt++; // 시간 증가
            }

            last = [startX, startY]; // 마지막 위치 기록
        }

        // 마지막 좌표 처리
        if (!time[cnt]) time[cnt] = {}; // 시간대마다 기록 초기화
        if (!time[cnt][last[0]]) time[cnt][last[0]] = {}; // 좌표별 기록 초기화
        if (!time[cnt][last[0]][last[1]]) time[cnt][last[0]][last[1]] = 0; // 로봇 수 초기화

        time[cnt][last[0]][last[1]] += 1; // 마지막 좌표에 로봇 도달

        // 충돌 체크: 한 위치에 로봇이 두 대 이상 있을 경우
        if (time[cnt][last[0]][last[1]] === 2) {
            answer++;
        }
    }

    // 각 로봇의 경로 계산
    for (let route of routes) {
        getAnswer(route);
    }

    return answer;
}















// function solution(points, routes) {
//   var answer = 0;
  
//   let map = new Map();
//   let timePos = [];
//   for(let i = 0; i<points.length; i++){
//     map.set(i + 1, [points[i][0], points[i][1]]);
//   }
    
//   function calcDanger(route){

//     let time = 0;
//     let last = [0,0];

//     for(let i = 0; i<route.length - 1; i++){
//       let [startX, startY] = map.get(route[i]);
//       let [destX, destY] = map.get(route[i + 1]);

//       while(startX !== destX || startY !== destY){

//         if(!timePos[time]) timePos[time] = {};
//         if(!timePos[time][startX]) timePos[time][startX] = {};
//         timePos[time][startX][startY] = (timePos[time][startX][startY] || 0 ) + 1;

//         if(timePos[time][startX][startY] === 2) answer++;

//         if(startX < destX) startX++;
//         else if(startX > destX) startX--
//         else if(startY < destY) startY++;
//         else if(startY > destY) startY--;
//         last = [startX, startY];

//         time++;
//       }
//     }

//     if(!timePos[time]) timePos[time] = {};
//     if(!timePos[time][last[0]]) timePos[time][last[0]] = {};
//     timePos[time][last[0]][last[1]] = (timePos[time][last[0]][last[1]] || 0) + 1;
//     if(timePos[time][last[0]][last[1]] === 2) answer++;
//   }

//   for(let r of routes){
//     calcDanger([...r]);
//   }
 
//   return answer;
// }
