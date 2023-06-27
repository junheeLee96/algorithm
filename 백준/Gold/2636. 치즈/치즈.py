from collections import deque


n, m = map(int, input().split())


arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)


dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


time = 0
ans = []


def bfs():
    q = deque()
    cnt = 0
    q.append((0, 0))
    visit[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if arr[nx][ny] == 0:
                    visit[nx][ny] = True
                    q.append((nx, ny))

                elif arr[nx][ny] == 1:
                    arr[nx][ny] = 0
                    visit[nx][ny] = True
                    cnt += 1

    ans.append(cnt)
    return cnt


while True:
    time += 1

    visit = [[False for _ in range(m)]for _ in range(n)]
    cnt = bfs()

    if cnt == 0:
        break

print(time - 1)
print(ans[-2])
