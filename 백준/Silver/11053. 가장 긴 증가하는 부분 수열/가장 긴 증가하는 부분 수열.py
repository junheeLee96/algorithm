from bisect import bisect_left

n = int(input())

arr = list(map(int, input().split()))

dp = []

for i in range(n):
    if not dp or dp[-1] < arr[i]:
        dp.append(arr[i])

    else:
        dp[bisect_left(dp, arr[i])] = arr[i]

print(len(dp))
