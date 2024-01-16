from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0

while True:
    bfs_visit = [[False for _ in range(m)] for _ in range(n)]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        bfs_visit[x][y] = True

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and bfs_visit[nx][ny] == False and arr[nx][ny] > 0:
                    bfs_visit[nx][ny] = True
                    q.append((nx, ny))

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0 and bfs_visit[i][j] == False:
                cnt += 1
                bfs(i, j)
    if cnt == 0:
        # answer = 0
        print(0)
        break
    # print('----------')
    # print(answer)
    # for i in arr:
    #     print(i)
    # print('----------')

    if cnt >= 2:
        print(answer)
        break

    answer += 1
    visit = [[False for _ in range(m)] for _ in range(n)]

    def check(x, y):
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] <= 0:
                cnt += 1

        return cnt

    visit = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if arr[i][j] > 0:
                cnt = check(i, j)
                visit[i][j] = cnt

    for i in range(n):
        for j in range(m):
            if visit[i][j] != 0:
                if arr[i][j] - visit[i][j] <= 0:
                    arr[i][j] = 0
                else:
                    arr[i][j] -= visit[i][j]


# print(answer)
