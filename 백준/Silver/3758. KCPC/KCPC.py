import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n,k,t,m=map(int,input().split())
    board=[[0]*k for _ in range(n)]
    count=[0]*n #제출횟수
    time=[0]*n #제출시간
    for ts in range(m):
        i,j,s=map(int,input().split())
        board[i-1][j-1]=max(board[i-1][j-1],s)
        time[i-1]=ts
        count[i-1]+=1
    new=[]
    for idx in range(len(board)):
        new.append([sum(board[idx]),count[idx],time[idx],idx])
    new.sort(key=lambda x:(-x[0],x[1],x[2])) #규칙대로정렬
    for idx in range(len(new)):
        if new[idx][3]==t-1:
            print(idx+1)
            break