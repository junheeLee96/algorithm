def solution(n, money):
    answer = 0
    dp = [0] * (n+1)
    
    dp[0] = 1
    for num in money:
        for idx in range(num,n+1):
            dp[idx] = dp[idx] + dp[idx - num]
    return (dp[-1]) 
    