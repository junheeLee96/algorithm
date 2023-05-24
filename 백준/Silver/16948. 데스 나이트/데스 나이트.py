from collections import deque

n = int(input())

arr = list(map(int, input().split()))

maps = [[0 for _ in range(n)] for _ in range(n)]

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque()
q.append((arr[0], arr[1]))

answer = -1

while q:

    x, y = q.popleft()

    if x == arr[2] and y == arr[3]:
        answer = maps[x][y]
        break

    for i in range(len(dx)):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if maps[nx][ny] == 0:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y]+1

print(answer)
