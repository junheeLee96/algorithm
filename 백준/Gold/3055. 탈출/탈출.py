from collections import deque

q = deque()

n, m = map(int, input().split())

arr = []
visit = [[0 for _ in range(m)]for _ in range(n)]

for i in range(n):
    arr.append(list(map(str, input().strip())))

gx = 0
gy = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == 'S':
            q.append((i, j))
        if arr[i][j] == 'D':
            gx, gy = i, j


for i in range(n):
    for j in range(m):
        if arr[i][j] == '*':
            q.append((i, j))

con = True
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(Dx, Dy):
    while q:
        x, y = q.popleft()
        if arr[Dx][Dy] == 'S':
            return visit[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and arr[x][y] == 'S':
                    arr[nx][ny] = 'S'
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                elif (arr[nx][ny] == '.' or arr[nx][ny] == 'S') and arr[x][y] == '*':
                    arr[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"


print(bfs(gx, gy))
