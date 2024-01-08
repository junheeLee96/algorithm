import sys
input = sys.stdin.readline

n = int(input())

arr = [0] + list(map(int, input().split()))

m = int(input())


dp = []


for i in range(len(arr)):
    if not dp:
        dp.append(arr[i])
    else:
        dp.append(arr[i] + dp[-1])

for _ in range(m):
    l, r = map(int, input().split())

    num = dp[r] - dp[l-1]

    print(num)
