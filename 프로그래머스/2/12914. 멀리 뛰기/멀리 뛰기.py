def solution(n):
    answer = 0
    
    dp= [0,1,2]
    if n < 3:
        return dp[n]
    
    for i in range(2,n):
        dp.append(dp[i] + dp[i-1])
    
    return dp[-1] % 1234567





























# def solution(n):
#     temp = dict()
    
#     temp[0] = 1
#     temp[1] = 1
        
#     for i in range(2, n+1):
#         temp[i] = temp[i-1] + temp[i-2]
    
#     answer = temp[n] % 1234567    
#     return answer