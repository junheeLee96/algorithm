
n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip())))


dp = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = arr[i][j]
        else:
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

answer = 0

for i in dp:
    for j in i:
        answer = max(answer, j)

print(answer * answer)