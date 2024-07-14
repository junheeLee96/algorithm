n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))


dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + arr[i][0] <= n:
        dp[i] = max(dp[i+1], dp[i+arr[i][0]] + arr[i][1])
    else:
        dp[i] = dp[i+1]

print(max(dp))
