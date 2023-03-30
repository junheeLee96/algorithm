def solution(name, yearning, photo):
    answer = []
    
    dic = {}
    ssum = 0
    for i in range(len(name)):
        if name[i] not in dic:
            dic[name[i]] = yearning[i]
        ssum += yearning[i]
        
    for i in range(len(photo)):
        count = 0 
        no = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                count += dic[photo[i][j]]
            
            
            
        answer.append(count)
    return answer