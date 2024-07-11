def solution(genres, plays):
    answer = []
    
    obj = {}
    
    for i in range(len(genres)):
        if genres[i] not in obj:
            obj[genres[i]] = [plays[i],[i,plays[i]]]
        else:
            obj[genres[i]][0] += plays[i]
            obj[genres[i]].append([i,plays[i]])
    arr = [i for i in obj.values()]
    arr.sort(key=lambda x: -x[0])
    
    for i in arr:
        new_arr = i[1:]
        new_arr.sort(key=lambda x : -x[1])
        answer.append(new_arr[0][0])
        if len(new_arr) >= 2:
            answer.append(new_arr[1][0])
        
            
        
    return answer