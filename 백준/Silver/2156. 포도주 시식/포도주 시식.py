n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

dp = [0] * 10000


dp[0] = arr[0]
if n > 1:
    dp[1] = arr[1] + arr[0]
if n > 2:
    dp[2] = max(arr[2] + arr[1], arr[2] + arr[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

    # 현재를 마시지 않을 때,
    # 전전꺼를 안마시고 현재와 전꺼를 마셨을 때,
    # 전꺼를 안마셨을 때,

print(dp[n-1])