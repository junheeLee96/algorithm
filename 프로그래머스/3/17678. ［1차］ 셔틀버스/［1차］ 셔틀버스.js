function solution(n, t, m, timetable) {
    var answer = '';
    timetable = timetable.map(a=> {
        const [h,m] = a.split(':').map(Number);
        return 60 * h + m
    });
    timetable.sort((a,b)=>a-b);
    
    let time = 9 * 60;
  for(let i = 1 ; i <= n ; i ++) {
        const canRide = timetable.filter(a => a <= time).length
        if(i === n) {
            if(canRide >= m) {
                time = timetable[m-1]-1
            }
        } else {
            timetable.splice(0,canRide > m ? m : canRide)
            time+=t
        }
    }
    
    return `${String(Math.floor(time /60)).padStart(2,'0')}:${String(time % 60).padStart(2,'0')}`
}