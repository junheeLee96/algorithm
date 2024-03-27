n, m, q = map(int, input().split())

arr = [[0 for _ in range(m)]]

for _ in range(n):
    l = [0] + list(map(int, input().split()))
    # print(l)
    arr.append(l)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i][j] - dp[i-1][j-1]

for _ in range(q):
    l = list(map(int, input().split()))

    x1, y1, x2, y2 = l[0], l[1], l[2], l[3]

    num = dp[x2][y2] + dp[x1-1][y1-1] - dp[x1 - 1][y2] - dp[x2][y1 - 1]

    div = ((x2 - x1) + 1) * ((y2 - y1) + 1)

    print(num // div)