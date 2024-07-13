t = int(input())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3


for i in range(7, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())

    print(dp[n])
