def solution(k, score):
    answer = []
    
    arr = []
    
    for i in range(len(score)):
        if k > 0:
            k-=1
            arr.append(score[i])
        else:
            if min(arr) < score[i]:
                arr.pop(arr.index(min(arr)))
                arr.append(score[i])
        answer.append(min(arr))
    return answer