function solution(m, n, puddles) {
    const dp = Array.from({ length: n }, () => Array.from({length:m},()=>0));
    for(let [y,x] of puddles){
        dp[x-1][y-1] = 'x';
    }
    for(let i =0; i < n; i ++){
        if(dp[i][0] === 'x') break;
        dp[i][0] = 1
    }
    for(let i =0; i <m; i++){
        if(dp[0][i] === 'x') break;
        dp[0][i] = 1
    }
    
    for(let i = 1; i <n; i++){
        for(let j = 1; j <m; j++){
            if(dp[i][j] !== 'x' && dp[i-1][j] === 'x'){
                dp[i][j] = dp[i][j-1]
            }else if (dp[i][j] !== 'x' && dp[i][j-1] === 'x'){
                dp[i][j] = dp[i-1][j];
            }
            else if(dp[i][j] !== 'x'){
                dp[i][j] = ( dp[i-1][j] + dp[i][j-1]) % 1000000007;
            }
        }
    }
    return dp[n-1][m-1] 
}
