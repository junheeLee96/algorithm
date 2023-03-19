def solution(cards1, cards2, goal):
    answer = ''
    
    isTrue = True
    
    for i in range(len(goal)):
        string = goal[i]
        c1 = ''
        c2 = ''
        if cards1:
            c1 = cards1[0] 
        
        if cards2:
            c2 = cards2[0]
        
        if c1 == string:
            cards1.pop(0)
        
        elif c2 == string:
            cards2.pop(0)
        
        else:
            isTrue = False
            break
            
    if isTrue == False:
        answer = 'No'
    else:
        answer = 'Yes'
        
            
        
    return answer