def solution(s):
    answer = True
    stack = []
    
    stack.append(s[0])
    
    for i in range(1,len(s)):
        if stack:
            if stack[-1] == '(':
                if s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
                
        else:
            stack.append(s[i])
    return False if stack else True

# def solution(s):
#     stack = []
#     for i in s:
#         if i =='(':
#             stack.append('(')
#         else:
#             if stack == []:
#                 return  False
#             else:
#                 stack.pop()
            
        
        
#     return stack == []