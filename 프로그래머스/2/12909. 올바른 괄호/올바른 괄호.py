def solution(s):
    
    answer = True
    stack = []
    
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)
    print(stack)
#     answer = True
#     stack = []
    
#     stack.append(s[0])
    
#     for i in range(1,len(s)):
#         if stack:
#             if stack[-1] == '(':
#                 if s[i] == ')':
#                     stack.pop()
#                 else:
#                     stack.append(s[i])
#             else:
#                 stack.append(s[i])
                
#         else:
#             stack.append(s[i])
    return False if stack else True
