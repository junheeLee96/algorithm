n = int(input())

arr = list(map(int, input().split()))
dp = [arr[0]]

for i in range(1, n):
    dp.append(max(arr[i], arr[i] + dp[i-1]))
print(max(dp))