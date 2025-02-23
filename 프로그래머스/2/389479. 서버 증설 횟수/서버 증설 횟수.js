function solution(players, m, k) {
    var answer = 0;
    let server = Array.from({length:24},()=>0);
    
    for(let i =0 ; i <players.length; i ++){
        if(i>0) server[i] += server[i-1];
        
        let need = Math.floor(players[i]/m - server[i]);
        if(need > 0){
            server[i] += need;
            answer += need;
            if(i + k < server.length){
                server[i+k] -= need
            }
        }
    }
    return answer;
}