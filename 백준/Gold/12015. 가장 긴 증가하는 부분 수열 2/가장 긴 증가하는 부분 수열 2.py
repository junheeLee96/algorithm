from bisect import bisect_left

n = int(input())

arr = list(map(int, input().split()))

dp = []

for i in arr:
    if not dp or dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp))
