def solution(triangle):
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    for i in range(len(triangle[-1])):
        dp[-1][i] = triangle[-1][i]

    for i in range(len(triangle)-1, 0, -1):
        for j in range(len(triangle[i])):
            
            if j < len(triangle[i-1]):
                dp[i-1][j] = max(dp[i][j] + triangle[i-1][j], dp[i-1][j])

            if j != 0:
                dp[i-1][j-1] = max(dp[i][j] + triangle[i-1][j-1], dp[i-1][j-1])

    return dp[0][0]