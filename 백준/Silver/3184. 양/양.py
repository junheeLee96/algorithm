from collections import deque

col,row = map(int,input().split())

arr = []

for i in range(col):
  a = str(input())
  a = list(a)
  arr.append(a)

visit = [[False]*row for _ in range(col)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
w,s = 0,0
for i in range(col):
  for j in range(row):
    if visit[i][j] == False:
      if arr[i][j] == 'v' or arr[i][j] =='o':
        wolf,sheep =0,0
        q = deque()
        q.append((i,j))
        visit[i][j] = True
        while q:
          x,y = q.popleft()
          if arr[x][y] == 'v':

            wolf += 1
          if arr[x][y] == 'o':
            sheep += 1
  
          for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < col and 0 <= ny < row:
              if visit[nx][ny] == False:
                if arr[nx][ny] != '#':
                  visit[nx][ny] = True
                  q.append((nx,ny))
        if wolf <sheep:
          s += sheep
        else:
          w += wolf
print(s,w)
          
                  