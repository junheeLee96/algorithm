n, k = map(int, input().split())

arr = []

dp = [0] * (k+1)
dp[0] = 1

for _ in range(n):
    arr.append(int(input()))

for num in arr:
    for idx in range(num, k + 1):
        dp[idx] = dp[idx] + dp[idx - num]


print(dp[k])
