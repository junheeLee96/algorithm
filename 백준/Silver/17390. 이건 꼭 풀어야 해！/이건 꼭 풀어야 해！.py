import sys
input = sys.stdin.readline

n, q = map(int, input().split())


arr = [0]+list(map(int, input().split()))
arr.sort()

dp = []

for i in arr:
    if not dp:
        dp.append(i)
    else:
        dp.append(dp[-1] + i)

# print(dp)

answer = []
for _ in range(q):
    l, r = map(int, input().split())

    right = dp[r]
    left = dp[l-1]
    # print(right, left)
    # break
    print(right - left)

# print(answer)
