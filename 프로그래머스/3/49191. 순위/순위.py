def solution(n, results):
    answer = 0
    grid=[[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for a, b in results:
        grid[a][b]=1
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if grid[i][j]==1 or (grid[i][k]==1 and grid[k][j]==1):
                    grid[i][j]=1
    
    answers=[0 for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if grid[i][j]==1:
                answers[i]+=1
                answers[j]+=1
    for i in range(1, n+1):
        if answers[i]==n-1:
            answer+=1
    return answer