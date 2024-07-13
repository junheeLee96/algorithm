import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1  # 출발점에서 출발하는 경우의 수는 1

for x in range(n):
    for y in range(n):
        if x == n - 1 and y == n - 1:
            break  # 도착점에는 더이상 이동하지 않으므로 생략
        jump = arr[x][y]
        if x + jump < n:
            dp[x + jump][y] += dp[x][y]
        if y + jump < n:
            dp[x][y + jump] += dp[x][y]

print(dp[-1][-1])
