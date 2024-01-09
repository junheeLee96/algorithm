r, c, t = map(int, input().split())

arr = []

for _ in range(r):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(c + 1)] for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(t):
    r1, c1, r2, c2 = map(int, input().split())

    num = dp[r2][c2] + dp[r1-1][c1-1] - dp[r1-1][c2] - dp[r2][c1-1]

    division = ((r2 - r1) + 1) * ((c2 - c1) + 1)

    print(num // division)
