def solution(numbers, target):
    answer = 0
    
    
    
    def dfs(idx, num,calc):
        nonlocal answer
        if idx > len(numbers) - 1:
            if num == target:
                answer += 1
            return
        
        if calc == '-':
            num = num - numbers[idx]
        else:
            num = num + numbers[idx]
        
        dfs(idx+1, num, '-')
        dfs(idx+1, num, '+')
    
    dfs(0, 0, '-')
    dfs(0, 0, '+')
    
    
    return answer//2