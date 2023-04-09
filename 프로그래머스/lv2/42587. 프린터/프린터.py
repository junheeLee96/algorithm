def solution(priorities, location):
    answer = 0
    
    goal = priorities[location]
    count = 0
    
    while True:
        if max(priorities) == priorities[0]:
            if location == 0:
                break
            else:
                priorities.pop(0)
                count += 1
                location -= 1
        else:
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
            
            priorities.append(priorities.pop(0))
    return count+1