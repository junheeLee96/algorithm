def solution(keymap, targets):
    answer = []
    obj = {}
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in obj:
                obj[keymap[i][j]] = j
            else:
                if obj[keymap[i][j]] > j:
                    obj[keymap[i][j]] = j
    
    for i in range(len(targets)):
        num = 0
        isTrue = True
        for j in range(len(targets[i])):
            if targets[i][j] not in obj:
                answer.append(-1)
                isTrue = False
                break
            else:
                num += obj[targets[i][j]]+1
        if isTrue:
            answer.append(num)
    return answer