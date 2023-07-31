from collections import deque

n = int(input())

max_area = 1

arr = [list(map(int, input().split()))for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(arr, height):
    visit = [[False] * n for _ in range(n)]
    area = 0
    for i in range(len(arr[0])):
        for j in range(len(arr[0])):
            if visit[i][j] == False and arr[i][j] > height:
                visit[i][j] = True
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()

                    for p in range(4):
                        nx = dx[p] + x
                        ny = dy[p] + y

                        if 0 <= nx < n and 0 <= ny < n:
                            if visit[nx][ny] == False:
                                if arr[nx][ny] > height:
                                    q.append((nx, ny))
                                    visit[nx][ny] = True
                area += 1

    return area


for i in range(1, 100):
    # for i in range(1, 100):
    area = bfs(arr, i)
    if area > max_area:
        max_area = area

print(max_area)
