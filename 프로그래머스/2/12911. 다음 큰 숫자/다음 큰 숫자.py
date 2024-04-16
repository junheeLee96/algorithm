def solution(n):
    answer = 0
    n_bin = bin(n)
    cnt = str(n_bin[2:]).count('1')
    nxt = n+1
    while True:
        nxt_bin = bin(nxt)
        nxt_cnt = str(nxt_bin[2:]).count('1')
        
        if cnt == nxt_cnt:
            answer = nxt
            break
        
        nxt += 1
        
    return answer





# def b(n):
#     a = []
#     while n >=1:
#         a.append(n % 2)
#         n = n//2
#     return a.count(1)
    
        

# def solution(n):
    
#     bn =b(n)
    
#     while True:
#         n += 1
#         xn = b(n)
#         if bn == xn:
#             break
#     return n