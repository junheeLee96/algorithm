from collections import deque

n, m, trash_count = map(int, input().split())

arr = [[0 for _ in range(m)]for _ in range(n)]
visit = [[False for _ in range(m)]for _ in range(n)]


trash_position = deque()

for i in range(trash_count):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    trash_position.append((x, y))
    arr[x][y] = 1

max_trash = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visit[x][y] = True
    count = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == False and arr[nx][ny] == 1:
                    visit[nx][ny] = True
                    q.append((nx, ny))
                    count += 1
    return count


while trash_position:
    x, y = trash_position.popleft()
    if visit[x][y] == False:
        trash = bfs(x, y)
        if trash > max_trash:
            max_trash = trash

print(max_trash)
