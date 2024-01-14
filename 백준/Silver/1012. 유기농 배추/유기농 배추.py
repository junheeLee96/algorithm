from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    n, m, k = map(int, input().split())

    visit = [[False for _ in range(m)] for _ in range(n)]
    arr = [[0 for _ in range(m)] for _ in range(n)]
    p = []
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a][b] = 1
        p.append([a, b])
    cnt = 0
    for i in p:
        x, y = i[0], i[1]

        if visit[x][y] == False:
            cnt += 1
            q = deque()
            q.append((x, y))
            visit[x][y] = True
            while q:
                x, y = q.popleft()
                for j in range(4):
                    nx = dx[j] + x
                    ny = dy[j] + y

                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visit[nx][ny] == False:
                        q.append((nx, ny))
                        visit[nx][ny] = True

    print(cnt)


for _ in range(t):
    bfs()
