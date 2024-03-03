import sys

input = sys.stdin.readline

n, k = map(int, input().split())

arr = [[0, 0]]

for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, k+1):
        w = arr[i][0]
        v = arr[i][1]

        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[n][k])