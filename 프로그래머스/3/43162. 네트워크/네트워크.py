from collections import deque

def solution(n, computers):
    answer = 0
    arr = [[] for _ in range(n)]
    
    visit = [False for _ in range(n)]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                arr[i].append(j)
    
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if visit[arr[i][j]] == False:
                cnt += 1
                visit[arr[i][j]] = True
                
                q = deque()
                q.append(arr[i][j])
                while q:
                    idx = q.popleft()
                    
                    for nxt in arr[idx]:
                        if visit[nxt] == False:
                            visit[nxt] = True
                            q.append(nxt)
                
        
    for i in visit:
        if i == False:
            cnt += 1
    
    return cnt