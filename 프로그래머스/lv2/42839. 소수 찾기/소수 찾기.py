from itertools import permutations

def isTrue(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    arr = list(numbers)
    
    check = []
    
    for i in range(1,len(numbers)+1):
        for j in permutations(arr,i):
            s = ''
            for k in j:
                s += k
            
            if int(s) != 1:
                if int(s) !=0:
                    if int(s) not in check:
                        check.append(int(s))
                        if isTrue(int(s)):
                            answer+=1
                
            
        
    return answer