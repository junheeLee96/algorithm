import copy
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
# 첫행은 누적으로 dp채워주기
dp[0] = copy.deepcopy(data[0])

for i in range(1, m):
    dp[0][i] += dp[0][i-1]

for i in range(1, n):
    tmp1 = [0]*m  # 왼쪽 > 오른쪽 최대값
    tmp2 = [0]*m  # 왼쪽 < 오른쪽 최대값

    for j in range(m):

        # 첫번째 칸은 그냥 갱신
        if j == 0:
            tmp1[j] = data[i][j] + dp[i-1][j]
            tmp2[m-1-j] = data[i][m-1-j] + dp[i-1][m-1-j]
            continue

        tmp1[j] = data[i][j] + max(dp[i-1][j], tmp1[j-1])
        tmp2[m-1-j] = data[i][m-1-j] + max(dp[i-1][m-1-j], tmp2[m-j])

    # tmp1과 tmp2 중 최대값을 dp에 갱신
    tmp = [max(tmp1[i], tmp2[i]) for i in range(m)]
    dp[i] = copy.deepcopy(tmp)

print(dp[n-1][m-1])
