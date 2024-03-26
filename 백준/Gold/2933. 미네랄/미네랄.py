import sys
import collections

# get_cluster : 클러스터 번호를 key, 클러스터에 속하는 미네랄의 좌표들의 리스트를 value로 하는 dict를 리턴하는 함수


def get_cluster():
    q = collections.deque()
    res = dict()

    # cnt : 각 클러스터 번호
    cnt = 1
    for i in range(n):
        for j in range(m):
            if check[i][j] == -1:
                if arr[i][j] == 'x':

                    # 아직 방문하지 않은 미네랄을 기준으로 bfs를 통해 클러스터 계산
                    q.append((i, j))
                    check[i][j] = cnt
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x + dx[k], y + dy[k]
                            if 0 <= nx < n and 0 <= ny < m:
                                if check[nx][ny] == -1:
                                    if arr[nx][ny] == 'x':
                                        q.append((nx, ny))
                                        check[nx][ny] = check[x][y]

                    # 클러스터 번호 증가
                    cnt += 1

    for i in range(n):
        for j in range(m):
            if check[i][j] != -1:
                # 클러스터 번호가 dict의 key에 있는지에 따라 처리
                if check[i][j] in res:
                    res[check[i][j]].append((i, j))
                else:
                    res[check[i][j]] = [(i, j)]
    return res

# go : get_cluster 함수의 리턴된 dict를 파라미터로 하고 공중에 뜬 클러스터를 아래로 내리는 함수


def go(d):
    # dist : 공중에 뜬 클러스터가 내려가야 할 거리를 저장하는 리스트
    #  이 때, inf값이라면 바닥에 붙은 클러스터
    dist = [9876543210] * (max(d.keys()) + 1)
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'x':

                # 현재 미네랄에서 위로 진행하면서 다른 클러스터에 붙은 미네랄 탐색
                x, y = i - 1, j
                cnt = 1
                meet = False
                while 0 <= x < n:
                    if arr[x][y] == 'x':
                        meet = True
                        break
                    else:
                        x -= 1
                        cnt += 1

                # 다른 클러스터의 미네랄을 만났을 경우, 거리 갱신
                if meet:
                    if check[x][y] != check[i][j]:
                        dist[check[x][y]] = min(dist[check[x][y]], cnt)

    for i in d:
        # 각 클러스터에 속한 좌표 리스트를 x좌표 기준 역순 정렬
        # 해당 클러스터가 바닥에 있는지 아닌지 판단하기 쉽게하기 위함
        d[i].sort(reverse=True)

        # 현재 클러스터의 가장 밑에 있는 미네랄의 x좌표가 바닥이라면 continue
        if d[i][0][0] == n - 1:
            continue
        for j in d[i]:
            x, y = j

            # 그림 2에서 본 예외처리 후 이동
            dist[check[x][y]] = min(dist[check[x][y]], n - x)
            if dist[check[x][y]] != 9876543210:
                arr[x][y] = '.'
                # Q : 왜 -1을 더해주는가?
                # A : -1을 더해주지 않으면 만나야 할 미네랄을 덮어씌우기 때문이다
                arr[x + dist[check[x][y]] - 1][y] = 'x'

# throw : 현재 x좌표에서 s의 홀짝성 따라 창을 던지는 함수
        #   s가 홀수면 왼쪽에서 오른쪽, 짝수면 반대로 진행


def throw(x, s):
    if s % 2 == 0:
        for i in range(m):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                break
    else:
        for i in range(m - 1, -1, -1):
            if arr[x][i] == 'x':
                arr[x][i] = '.'
                break


# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
size = int(sys.stdin.readline())
info = list(map(int, sys.stdin.readline().split()))

# 전체 창을 던진 횟수에 따라 진행
for i in range(size):
    check = [[-1] * m for _ in range(n)]
    throw(n - info[i], i)
    temp = get_cluster()
    go(temp)

# 정답 출력
for i in arr:
    print(''.join(i))
