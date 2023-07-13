from collections import deque
import copy


def solution(maps):

    s = []
    l = []
    exit = []

    answer = 0
    visit = [[int(0) for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = [i, j]
                q = deque()  # q 변수 정의 및 초기화
                q.append((i, j))

            elif maps[i][j] == 'E':
                exit = [i, j]
            elif maps[i][j] == 'L':
                l = [i, j]
    # visit[s[0]][s[1]] = True
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    def bfs1(w, h, coin):
        bfs1visit = copy.deepcopy(visit)
        q = deque()  # q 변수 정의 및 초기화
        q.append((w, h))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'E':
                        if bfs1visit[nx][ny] == 0:
                            bfs1visit[nx][ny] = bfs1visit[x][y] + 1
                            q.append((nx, ny))
                    elif maps[nx][ny] == 'L':
                        return bfs1visit[x][y] + 1

        return -1

    lebor = bfs1(s[0], s[1], 0)

    if lebor == -1:
        return -1

    visit[l[0]][l[1]] = lebor

    def bfs(w, h):
        q = deque()  # q 변수 정의 및 초기화
        q.append((w, h))

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y

                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                    if maps[nx][ny] == 'O' or maps[nx][ny] == 'S':
                        if visit[nx][ny] == 0:
                            visit[nx][ny] = visit[x][y] + 1
                            q.append((nx, ny))
                    elif maps[nx][ny] == 'E':
                        return visit[x][y] + 1

        return -1

    answer = bfs(l[0], l[1])
    return answer

