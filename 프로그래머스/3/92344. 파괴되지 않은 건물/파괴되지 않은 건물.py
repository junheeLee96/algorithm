def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    
    delta = [[0 for _ in range(m+1)]  for _ in range(n+1)]
    
    for s in skill:
        degree = s[5] if s[0] == 2 else -s[5]
        r1,c1,r2,c2 = s[1],s[2],s[3],s[4]
        
        delta[r1][c1] += degree
        delta[r1][c2+1] += -degree
        delta[r2+1][c1] += -degree
        delta[r2+1][c2+1] += degree
        
    # for c in range(m):
    #     for r in range(1, n):
    #         delta[r][c] += delta[r - 1][c]
    # for r in range(n):
    #     for c in range(1, m):
    #         delta[r][c] += delta[r][c - 1]
            
    for j in range(m):
        for i in range(1,n):
            delta[i][j] += delta[i-1][j]
    for i in range(n):
        for j in range(1,m):
            delta[i][j] += delta[i][j-1]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += delta[i][j]
            
            if board[i][j] >0 :
                answer += 1
    
#     delta = [[0] * (m+1) for _ in range(n+1)]
    
#     for s in skill:
#         t,sr,sc,er,ec,degree = s
#         if t == 1:
#             degree = -degree
        
#         delta[sr][sc] += degree
#         delta[sr][ec+1] += degree
#         delta[er+1][sc] += degree
#         delta[er + 1][ec + 1] += degree
        
        
#     for c in range(m):
#         for r in range(1,n):
#             delta[r][c] += delta[r-1][c]
            
#     for r in range(n):
#         for c in range(1,m):
#             delta[r][c] += delta[r][c-1]
            
    
#     for i in range(n):
#         for j in range(m):
#             board[i][j] += delta[i][j]
            
#             if board[i][j] > 0:
#                 answer += 1
            
    return answer