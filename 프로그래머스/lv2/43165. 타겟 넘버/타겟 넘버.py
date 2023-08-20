def solution(numbers, target):
    answer = 0
    max_idx = len(numbers) 
    
    
    def dfs (condition, idx,number):
    
        if idx == max_idx:
            if number == target :
                nonlocal answer 
                answer += 1
                return
        
            else:
                return 
        
        
        
        if condition:
            number += numbers[idx]
        else:
            number -= numbers[idx]
        
        idx += 1
        
        dfs(False, idx, number)
        dfs(True,idx,number)
        
        
#         False는 빼기, True는 덧셈
    dfs (False, 0, 0)
    dfs (True, 0, 0)
    return answer//2