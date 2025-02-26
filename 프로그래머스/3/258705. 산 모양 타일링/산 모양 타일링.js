function solution(n, tops) {
    var answer = 0;
    let MOD = 10007
    
    let length = n * 2 + 1;
    let dp = Array.from({length:length+1},()=>0);
    
    dp[0] = 1
    dp[1] = 1
    
    for(let i = 2 ; i < length + 1; i ++){
        if(i % 2 == 0 && tops[Math.floor((i-1) / 2)] === 1){
            dp[i] = (dp[i-1] * 2 + dp[i-2]) % MOD;
        }else{
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        }
    }
    return dp[dp.length-1] 
}