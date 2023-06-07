from collections import deque
def solution(x, y, n):
    dis = [0 for _ in range(y+1)]
    Q = deque()
    Q.append(x)
    if x == y:
        return 0
    while Q:
        nx = Q.popleft()
        for dir in range(3):
            if dir == 0:
                cur_x = nx * 2
            if dir == 1:
                cur_x = nx * 3
            if dir == 2:
                cur_x = nx + n
            if cur_x > y or dis[cur_x]:
                continue
            if cur_x == y:
                return dis[nx] + 1
            Q.append(cur_x)
            dis[cur_x] = dis[nx] + 1
    
    return -1