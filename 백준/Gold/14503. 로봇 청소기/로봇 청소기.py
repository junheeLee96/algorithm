import sys
input = sys.stdin.readline

graph = []
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
for _ in range(n):
    graph.append(list(map(int, input().split())))

graph[r][c] = -1
count = 1
while graph[r][c] != 1:
    temp = False
    for _ in range(4):
        d -= 1
        if d == -1:
            d = 3
        nr = r + dr[d]
        nc = c + dc[d]
        if graph[nr][nc] == 0:
            r = nr
            c = nc
            graph[r][c] = -1
            count += 1
            temp = True
            break
    if not temp:
        r += dr[d-2]
        c += dc[d-2]

print(count)
