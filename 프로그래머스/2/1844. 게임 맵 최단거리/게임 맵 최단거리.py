from collections import deque

def solution(maps):
    answer = 0
    arr = maps
    n = len(maps)
    m = len(maps[0])
    
    q = deque()
    q.append((0,0))
    dx= [ 0,0,1,-1]
    dy = [-1,1,0,0]
    
    visit = [[-1 for _ in range(m)] for _ in range(n)]
    visit[0][0] = 0
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == -1 and arr[nx][ny] == 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))
    if visit[n-1][m-1] == -1:
        return -1
    else:
        return visit[n-1][m-1]+1
