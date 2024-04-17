def solution(s):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    
    stack = []
    
    for i in s:
        if not stack or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
    if stack:
        answer = 0
    else:
        answer = 1
    
    return answer