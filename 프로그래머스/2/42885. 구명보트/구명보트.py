from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    q = deque(people)
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            answer+=1
        else:
            q.popleft()
            answer += 1
        
    if q:
        answer += 1
    
    return answer




















# from collections import deque
# def solution(people, limit):
#     answer = 0
#     arr = deque(sorted(people, reverse = True))
    
#     while len(arr) > 1:
#         if arr[0] + arr[-1] <= limit:
#             arr.pop()
#             arr.popleft()
#             answer+=1
        
#         else:
#             arr.popleft()
#             answer+=1
#     if arr:
#         answer+=1
    
    
        
        
        
            
            
        
#     return answer