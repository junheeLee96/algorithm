from collections import deque

n = int(input())

arr = []

for i in range(n):
    arr.append(str(input()))


visit = [[False for _ in range(n)] for _ in range(n)]

q = deque()

q.append((0, 0, 0))

visit[0][0] = True

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    x, y, cnt = q.popleft()

    if x == n-1 and y == n-1:
        print(cnt)
        break

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False:
                visit[nx][ny] = True
                if arr[nx][ny] == '1':
                    q.appendleft((nx, ny, cnt))
                else:
                    q.append((nx, ny, cnt+1))
