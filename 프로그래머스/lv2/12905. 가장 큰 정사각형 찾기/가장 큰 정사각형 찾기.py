def solution(board):
    answer = 0

    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    
    for i in board:
        mm = max(i)
        if answer < mm:
            answer = mm
    return answer ** 2