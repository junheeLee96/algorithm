from collections import deque


n, m = map(int, input().split())

sx, sy, gx, gy = map(int, input().split())

sx, sy, gx, gy = sx-1, sy-1, gx-1, gy-1

arr = []

for _ in range(n):
    arr.append(list(input().strip()))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

q = deque()

visit = [[-1 for _ in range(m)] for _ in range(n)]
visit[sx][sy] = 1
q.append((sx, sy))

while q:

    x, y = q.popleft()

    # if x == gx and y == gy:
    #     break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == -1:
            if arr[nx][ny] == '0':
                q.appendleft((nx, ny))
                visit[nx][ny] = visit[x][y]
            else:
                q.append((nx, ny))
                visit[nx][ny] = visit[x][y] + 1
print(visit[gx][gy] - 1)
