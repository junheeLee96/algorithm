from collections import deque



def solution(n, m, section):
    answer = 1
    number = section[0] + m - 1
    
    for i in range(1,len(section)):
        if section[i] <= number:
            continue
        
        else:
            number = section[i] + m - 1
            answer += 1
    return answer