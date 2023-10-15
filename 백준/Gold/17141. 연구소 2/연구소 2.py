from itertools import combinations
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
vi = []

for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
    for j in range(len(l)):
        if l[j] == 2:
            vi.append([i, j])
result = float('inf')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(vir):
    q = deque()
    cnt = 0
    visit = [[-1 for _ in range(n)]for _ in range(n)]

    for v in vir:
        q.append((v[0], v[1]))
        visit[v[0]][v[1]] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == -1 and arr[nx][ny] != 1:
                    q.append((nx, ny))
                    visit[nx][ny] = visit[x][y] + 1
                    cnt = max(cnt, visit[nx][ny])

    for i in range(len(visit)):
        for j in range(len(visit[0])):
            if visit[i][j] == -1 and arr[i][j] != 1:
                return 10000
    return cnt


for virus in combinations(vi, m):
    result = min(result, bfs(virus))

if result > 1000:
    print(-1)
else:
    print(result)
