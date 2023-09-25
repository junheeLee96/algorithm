from collections import deque
H,W = map(int,input().split())
field = list()
direction = [[0,1],[1,0],[-1,0],[0,-1]]

for _ in range(H):
    field.append(list(input()))
def bfs(rx,ry):
    visited = [[0]*W for _ in range(H)]
    q = deque([[rx,ry]])    
    visited[ry][rx]=1
    maxcnt = 0
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = dx+x,dy+y
            if 0<=nx<W and 0<=ny<H and field[ny][nx]=='L' and visited[ny][nx]==0:
                visited[ny][nx]=visited[y][x]+1
                if maxcnt < visited[ny][nx]:maxcnt=visited[ny][nx]
                q.append([nx,ny])
    return maxcnt-1
answer = 0
for i in range(H):
    for j in range(W):
        if field[i][j]=='L':
            tmp = bfs(j,i)
            if tmp>answer:
                answer = tmp
print(answer)