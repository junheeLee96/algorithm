def solution(n, words):
    number, order = 0,0
    arr= []
    arr.append(words[0])

    for i in range(1,len(words)):
        if words[i] not in arr and arr[-1][-1] == words[i][0]:
            arr.append(words[i])
        else:
            number = i % n + 1
            order = i // n + 1
            break
        

    return [number,order]