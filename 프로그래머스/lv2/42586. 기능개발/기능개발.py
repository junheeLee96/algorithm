def solution(progresses, speeds):
    answer = []
    
    day = 1
    count = 0
    
    while progresses:
        
        if progresses[0] + (speeds[0] * day) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count >= 1:
                answer.append(count)
            count = 0
            day += 1
    if count >= 1:
        answer.append(count)
            
    return answer