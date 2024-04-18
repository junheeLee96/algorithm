def solution(n, words):
    
    obj = {}
    answer = []
    
    obj[words[0]] = 0
    turn = 1
    for idx in range(1,len(words)):
        word = words[idx]
        prev = words[idx-1]
        
        if word[0] != prev[-1] or word in obj:
            
            answer = [idx % n + 1, turn]
            break
        
        obj[word] = 0
        
        if (idx +1) % n ==0 :
            print(idx,n)
            turn += 1
            
        
        
        
        
    if not answer:
        answer = [0,0]
    return answer






















# def solution(n, words):
#     number, order = 0,0
#     arr= []
#     arr.append(words[0])

#     for i in range(1,len(words)):
#         if words[i] not in arr and arr[-1][-1] == words[i][0]:
#             arr.append(words[i])
#         else:
#             number = i % n + 1
#             order = i // n + 1
#             break
        

#     return [number,order]