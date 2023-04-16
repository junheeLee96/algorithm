def solution(players, callings):
    answer = []
    
    dic = {}
    
    for i in range(len(players)):
        dic[players[i]] = i
    
    for i in range(len(callings)):
        idx = dic[callings[i]]
        
        temp = dic[callings[i]]
        dic[callings[i]] = dic[players[idx - 1]]
        dic[players[idx - 1]] = temp
        players[idx],players[idx-1] = players[idx-1],players[idx]
    return players