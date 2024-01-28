from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

cnt = 0


def bfs():
    visit = [[False for _ in range(m)] for _ in range(n)]
    visit[0][0] = True
    q = deque()

    q.append((0, 0))

    lists = []

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False:
                if arr[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                elif arr[nx][ny] == 1:
                    visit[nx][ny] = True
                    lists.append([nx, ny])

    return lists
# while True:


last = 0

while True:
    cnt += 1
    lists = bfs()

    if lists == []:
        break

    last = len(lists)

    for i in lists:
        x, y = i[0], i[1]

        arr[x][y] = 0

print(cnt-1, last)
