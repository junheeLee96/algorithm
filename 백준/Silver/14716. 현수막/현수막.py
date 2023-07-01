import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())

arr = []

dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, -1, 1, -1, 1]

one = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


visit = [[False for _ in range(m)] for _ in range(n)]

cnt = 0


def dfs(x, y):
    visit[x][y] = True

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] == False:
                if arr[nx][ny] == 1:
                    dfs(nx, ny)


for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 1 and visit[i][j] == False:
            dfs(i, j)
            cnt += 1

print(cnt)
