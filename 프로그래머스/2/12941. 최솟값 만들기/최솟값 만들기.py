def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer = answer + (A[i] * B[i])
    print(answer)
#     answer = 0

#     A.sort()
#     B.sort(reverse=True)
    
#     while A:
#         a = A.pop(0)
#         b = B.pop(0)
#         answer += a*b

    return answer