def solution(n):
    answer = 0
    s = 0
    
    for i in range(1,n+1):
        s = 0
        for j in range(i,n+1):
            s += j
            
            if s == n:
                answer += 1
                s = 0
                break
            elif s > n :
                break
            
    
#     for i in range(1,n+1):
#         sum = 0
#         for j in range(i,n+1):
#             sum += j
#             if sum == n:
#                 sum = 0
#                 answer +=1
#                 break;
#             elif sum >n:
#                 break
            
        
    return answer