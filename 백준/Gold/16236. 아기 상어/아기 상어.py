from collections import deque

n = int(input())

arr = []

shark_size = 2
eat = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

shark_x = 0
shar_y = 0
for i in range(n):
    a = (list(map(int, input().split())))
    for j in range(len(a)):
        if a[j] == 9:
            a[j] = 0
            shark_x = i
            shark_y = j
    arr.append(a)


def finding(x, y):
    q = deque()

    q.append((x, y))

    visit = [[False for _ in range(n)] for _ in range(n)]
    distance = [[0 for _ in range(n)] for _ in range(n)]

    can_eat_list = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= shark_size and not visit[nx][ny]:
                    visit[nx][ny] = True
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))

                    if arr[nx][ny] < shark_size and arr[nx][ny] != 0:
                        can_eat_list.append((nx, ny, distance[nx][ny]))

    can_eat_list.sort(key=lambda x: (x[2], x[0], x[1]))

    return can_eat_list


ans = 0

while True:
    fishlist = finding(shark_x, shark_y)

    if len(fishlist) == 0:
        print(ans)
        break

    shark_x, shark_y, move_time = fishlist[0]

    eat += 1
    if shark_size == eat:
        eat = 0
        shark_size += 1

    arr[shark_x][shark_y] = 0

    ans += move_time
