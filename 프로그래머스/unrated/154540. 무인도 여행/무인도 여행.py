from collections import deque

def solution(maps):
    answer = []
    visit = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visit[i][j] == False and maps[i][j] != 'X':
                visit[i][j] = True
                num = 0 
                q = deque()
                q.append((i,j))
                while q:
                    
                    x,y = q.popleft()
                    num = num + int(maps[x][y])
                    for k in range(4):
                        nx = dx[k] + x
                        ny = dy[k] + y
                        if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])):
                            if maps[nx][ny] != 'X' and visit[nx][ny] == False:
                                visit[nx][ny] = True
                                q.append((nx,ny))
                answer.append(num)
    answer.sort()
    return answer if len(answer) >0 else [-1]




# def solution(maps):
#     answer = []
    
#     visit = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
#     answer = []
    
    
    
#     dx = [1,-1,0,0]
#     dy = [0,0,-1,1]
#     def dfs(x,y,cnt):
#         visit[x][y] = True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and maps[nx][ny] != 'X':
#                 if visit[nx][ny] == False:
#                     cnt = dfs(nx,ny,cnt + int(maps[nx][ny]))
#         return cnt
        
    
#     for i in range(len(maps)):
#         for j in range(len(maps[0])):
#             cnt = 0
#             if visit[i][j] == False:
#                 if maps[i][j] != 'X':
#                     cnt = dfs(i,j,int(maps[i][j]))
                    
#                     answer.append(cnt)

#     answer.sort()
#     return [-1] if len(answer) == 0 else  answer