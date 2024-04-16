def f(num):
    if num == 1:
        return 1
    if num == 0:
        return 0
    
    return f(num-1) + f(num - 2)

def solution(n):
    dp = [0,1]
    for i in range(2,n+1):
        num = dp[-1] + dp[-2]
        dp.append(num)
        
    # answer = f(n)
    # print(dp[n])
    return dp[n] % 1234567




# def solution(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return a % 1234567