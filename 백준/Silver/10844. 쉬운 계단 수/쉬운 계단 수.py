n = int(input())

dp = [[1] * 10 for _ in range(n+1)]

dp[1][0] = 0
if n == 1:
    print(9)
else:
    dp = [[0] * 12 for _ in range(n+1)]

    dp[1][2:11] = [1] * 9

    for i in range(2, n+1):
        for j in range(1, 11):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    ans = sum(dp[n])

    print(ans % 1000000000)
