from bisect import bisect_left

n = int(input())

arr = []

for _ in range(n):
    arr.append(int(input()))

dp = []

for i in range(len(arr)):
    if not dp:
        dp.append(arr[i])

    else:
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]

print(n - len(dp))
