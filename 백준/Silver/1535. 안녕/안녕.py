import sys
input = sys.stdin.readline


n = int(input())
arr = [0]+list(map(int, input().split()))

happy = [0] + list(map(int, input().split()))


dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, 101):
        hap = happy[i]
        hp = arr[i]

        if hp > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], hap + dp[i-1][j-hp])

print(dp[n][99])
