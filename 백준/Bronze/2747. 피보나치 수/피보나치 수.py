n = int(input())

dp = [0, 1, 1]

if n <= 2:
    print(dp[n])
else:
    for i in range(n):
        dp.append(dp[-1] + dp[-2])

    print(dp[n])
