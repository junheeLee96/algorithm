from collections import Counter

def solution(s):
    answer = []
    s = s.replace('{','')
    s = s.replace('}','')
    s = list(s.split(','))
    c = Counter(s)
    sc = sorted(c.items(), key=lambda x:x[1])
    
    for i in range(len(sc)-1,-1, -1):
        a = int(sc[i][0])
        answer.append(a)
    return answer