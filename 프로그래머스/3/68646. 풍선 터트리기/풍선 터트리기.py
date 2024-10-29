import heapq

def solution(a):
    mx = 9999999999999
    answer = 2
    
    m = a.index(min(a))
    
    for i in range(m):
        if a[i] < mx:
            answer += 1
            mx = a[i]
    
    mx = 9999999999999
    
    for i in range(len(a)-1,m,-1):
        if a[i] < mx:
            answer += 1
            mx = a[i]
        
    
    
    
    return answer-1