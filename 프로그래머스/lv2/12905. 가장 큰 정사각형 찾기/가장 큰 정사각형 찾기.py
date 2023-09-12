# from collections import deque


# def solution(board):
#     answer = 1

#     def bfs(i, j):
#         q = deque()

#         area = 1

#         q.append((i, j))

#         while q:
#             x, y = q.popleft()

#             nx = x - 1
#             ny = y - 1

#             if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
#                 if board[nx][y] == 1 and board[x][ny] == 1:
#                     if board[nx][ny] == 1:
#                         q.append((nx, ny))
#                         area += 1

#         return area

#     for i in range(len(board)-1, -1, -1):
#         for j in range(len(board[0])-1, -1, -1):
#             if board[i][j] == 1:
#                 area = bfs(i, j)
#                 if area > answer:
#                     answer = area
#     return answer ** 2


def solution(board):
    n = len(board)
    m = len(board[0])

    # dp 준비
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]
    
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    
    return answer**2

