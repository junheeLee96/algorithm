from collections import deque
from itertools import combinations
import copy
n, m = map(int, input().split())


empty = []
virus = []
wall = []

arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
    for j in range(len(a)):
        if a[j] == 2:
            virus.append([i, j])
        elif a[j] == 1:
            wall.append([i, j])
        else:
            empty.append([i, j])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

max_cnt = 0

for i in combinations(empty, 3):
    # print(i[0])
    # cnt += 1
    cnt = 0
    graph = copy.deepcopy(arr)
    # graph[i[0][0]][i[0][1]] =
    one = i[0]
    tow = i[1]
    three = i[2]

    # print(one)
    graph[one[0]][one[1]] = 1
    graph[tow[0]][tow[1]] = 1
    graph[three[0]][three[1]] = 1

    q = deque()

    for v in virus:
        q.append((v[0], v[1]))

    while q:
        x, y = q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = 2

    for col in graph:
        for row in col:
            if row == 0:
                cnt += 1

    if max_cnt < cnt:
        # print(i)
        max_cnt = cnt


print(max_cnt)
