from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(board, h, w):
    n = len(board)
    m = len(board[0])
    answer = 0
    color = board[h][w]
    cnt = 0
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]

        if 0 <= nx < n and 0 <= ny < m and color == board[nx][ny]:
            cnt += 1

    answer = cnt

    return answer
