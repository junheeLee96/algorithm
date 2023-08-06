from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

max_area = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    area = 1
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append((nx, ny))
                    arr[nx][ny] = 0
                    area += 1

    return area

cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = 0
            area = bfs(i, j)
            cnt += 1
            if max_area < area:
                max_area = area

print(cnt)
print(max_area)