# def solution(s):
#     answer = ''
#     arr = list(int(i) for i in s.split())
#     answer += min(arr)
#     answer += max(Arr)
#     return answer

def solution(s):
    answer =''
    arr = list(int(i) for i in s.split())
    print(arr)
    mi = min(arr)
    mn = max(arr)
    answer = str(mi) + ' ' + str(mn)
    return answer