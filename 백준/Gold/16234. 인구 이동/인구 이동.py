from collections import deque
from copy import deepcopy

n, l, r = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    ar = deepcopy(arr)
    visit = [[False for _ in range(n)]for _ in range(n)]
    returnValue = []
    for i in range(n):
        for j in range(n):
            if visit[i][j] == False:
                q = deque()
                visit[i][j] = True
                q.append((i, j))
                contries = [[i, j]]
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < n:
                            if visit[nx][ny] == False:
                                if l <= abs(ar[x][y] - ar[nx][ny]) <= r:
                                    q.append((nx, ny))
                                    visit[nx][ny] = True
                                    contries.append([nx, ny])
                if (len(contries) != 1):
                    returnValue.append(contries)

    # returnValue = [value for value in returnValue if len(value) != 1]
    return returnValue


answer = 0

while True:

    contry_arr = bfs()

    if not contry_arr:
        # print(contry_arr)
        break

    else:
        for i in contry_arr:
            s = 0
            for j in range(len(i)):

                s += arr[i[j][0]][i[j][1]]
            avg = s // len(i)
            for j in range(len(i)):
                arr[i[j][0]][i[j][1]] = avg
        answer += 1

print(answer)
