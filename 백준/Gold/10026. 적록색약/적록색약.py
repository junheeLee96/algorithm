from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(str, input().strip())))


visit = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False and arr[nx][ny] == arr[x][y]:
                q.append((nx, ny))
                visit[nx][ny] = True


for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            cnt += 1
            visit[i][j] = True
            bfs(i, j)


for i in range(n):
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

visit = [[False for _ in range(n)] for _ in range(n)]


cnt2 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            cnt2 += 1
            visit[i][j] = True
            bfs(i, j)

print(cnt, cnt2)
