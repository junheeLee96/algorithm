from collections import deque
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(y, x, visited, land, cnt, rows, cols):
    q = deque()
    q.append([y, x])
    visited[y][x] = cnt
    count = 1

    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if ny < 0 or ny >= cols or nx < 0 or nx >= rows:
                continue
            if visited[ny][nx] == 0 and land[ny][nx] == 1:
                visited[ny][nx] = cnt
                q.append([ny, nx])
                count += 1
    return count


def solution(land):
    cnt = 1
    answer = []
    val = {}
    rows = len(land[0])
    cols = len(land)
    visited = [[0] * rows for _ in range(cols)]
    for x in range(rows):
        for y in range(cols):
            if visited[y][x] == 0 and land[y][x] == 1:
                val[cnt] = bfs(y, x, visited, land, cnt, rows, cols)
                cnt += 1
    for x in range(rows):
        tmp2 = 0
        tmp = set()
        for y in range(cols):
            if visited[y][x] != 0:
                tmp.add(visited[y][x])
        for i in tmp:
            tmp2 += val[i]
        answer.append(tmp2)

    return max(answer)

