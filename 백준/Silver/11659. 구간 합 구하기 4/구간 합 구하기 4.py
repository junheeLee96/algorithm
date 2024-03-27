import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr = [0] + arr

dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = arr[i] + dp[i-1]


for _ in range(m):
    i, j = map(int, input().split())

    print(dp[j]-dp[i-1])
