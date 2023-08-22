from copy import deepcopy
from collections import deque
n, m = map(int, input().split())

origin_arr = []

for i in range(n):
    origin_arr.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, visit, melt_arr, arr):
    visit[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] >= 1:
                arr[nx][ny] += 1

                if arr[nx][ny] == 3:
                    melt_arr.append((nx, ny))

            else:
                if visit[nx][ny] == False:
                    visit[nx][ny] = True
                    dfs(nx, ny, visit, melt_arr, arr)


def bfs(i, j,  arr):
    q = deque()
    visit = [[False for _ in range(m)]for _ in range(n)]
    visit[i][j] = True
    melts = []
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] >= 1:
                    arr[nx][ny] += 1

                    if arr[nx][ny] == 3:
                        melts.append((nx, ny))

                else:
                    if visit[nx][ny] == False:
                        visit[nx][ny] = True
                        q.append((nx, ny))

    return melts


time = 0
while True:

    # visit = [[False for _ in range(m)]for _ in range(n)]
    arr = deepcopy(origin_arr)
    # melt_arr = []
    # dfs(0, 0, visit, melt_arr, arr)
    melt_arr = bfs(0, 0, arr)
    if not melt_arr:
        break
    else:
        for i in range(len(melt_arr)):
            origin_arr[melt_arr[i][0]][melt_arr[i][1]] = 0

        time += 1

print(time)
