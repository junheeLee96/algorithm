from collections import deque
import sys
input = sys.stdin.readline

k = int(input())

w, h = map(int, input().split())
w, h = h, w

arr = []

for _ in range(w):
    arr.append(list(map(int, input().split())))


# visit = [[[0] * k+1 for _ in range(h)] for _ in range(w)]
visit = [[[0] * (k + 1) for _ in range(h)] for _ in range(w)]
# print(visit[0][0][0])
# print('----')
visit[0][0][0] = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]

q = deque()
q.append((0, 0, 0))

condition = True

while q:
    # print(q)
    x, y, z = q.popleft()

    if x == w - 1 and y == h-1:
        condition = False
        print(visit[x][y][z] - 1)
        break

    if z < k:
        for i in range(8):
            nx = x + hx[i]
            ny = y + hy[i]
            # print(z)
            if 0 <= nx < w and 0 <= ny < h:
                # for q in visit:
                # print(q)
                if visit[nx][ny][z+1] == 0:
                    if arr[nx][ny] == 0:
                        q.append((nx, ny, z+1))
                        visit[nx][ny][z+1] = visit[x][y][z] + 1
            # if 0 <= nx < w and 0 <= ny < h and visit[nx][ny][z+1] == 0 and arr[nx][ny] == 0:
            #     q.append((nx, ny, z+1))
            #     visit[nx][ny][z+1] = visit[x][y][z] + 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < w and 0 <= ny < h and visit[nx][ny][z] == 0:
            if arr[nx][ny] == 0:
                q.append((nx, ny, z))
                visit[nx][ny][z] = visit[x][y][z] + 1

if (condition):
    print(-1)
