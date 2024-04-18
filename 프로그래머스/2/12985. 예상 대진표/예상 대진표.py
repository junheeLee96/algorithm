def solution(n,a,b):
    answer = 0
    
    turn  = 1
    while True:
        if a %2 != 0:
            a += 1
        if b % 2 != 0:
            b += 1
        
        a = a // 2
        b = b // 2
        
        if a == b:
            break
        turn += 1

    return turn








# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a,b = (a+1) // 2 , (b+1) // 2
#         print(a,b)

#     return answer