t = int(input())


for _ in range(t):
    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    n = int(input())
    if n <= 10:
        print(dp[n])
    else:
        for i in range(11, n+2):
            num = dp[-2] + dp[-3]
            dp.append(num)
        print(dp[n])