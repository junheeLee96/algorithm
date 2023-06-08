from bisect import bisect_left


n = int(input())
arr = list(map(int, input().split(" ")))

dp = [arr[0]]

for i in range(1, len(arr)):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
    else:
        idx = bisect_left(dp, arr[i])
        dp[idx] = arr[i]


print(n - len(dp))
