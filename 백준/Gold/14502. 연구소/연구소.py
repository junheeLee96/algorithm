import sys
from itertools import combinations
from copy import deepcopy
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
arr = []
empty = []
wall = []
vi = []

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(n):
    l = list(map(int, input().split()))
    arr.append(l)
    for j in range(m):
        if l[j] == 0:
            empty.append([i, j])

        if l[j] == 1:
            wall.append([i, j])

        if l[j] == 2:
            vi.append([i, j])


def func(lst):

    cop = deepcopy(arr)

    # print(cop)
    for i in lst:
        # print(i)
        x, y = i[0], i[1]
        # print(f'x = {x} y = {y}')
        cop[x][y] = 1
    # return

    visit = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if cop[i][j] == 2:

                q = deque()
                q.append((i, j))
                visit[i][j] = True

                while q:

                    x, y = q.popleft()
                    # cop[x][y] = 2
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == False and cop[nx][ny] == 0:
                            visit[nx][ny] = True
                            q.append((nx, ny))
    cnt = 0

    for i in range(n):
        for j in range(m):
            if visit[i][j] == False and cop[i][j] != 1:
                cnt += 1
    # print(lst)
    # for i in visit:
    #     print(i)

    return cnt


answer = 0

for lst in combinations(empty, 3):
    cnt = func(lst)
    # break
    answer = max(answer, cnt)
    # break

print(answer)
