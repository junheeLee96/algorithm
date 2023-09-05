from collections import deque

def solution(picks, minerals):
    answer = 0
    pickable_minerals = minerals[: sum(picks) * 5]
    tools_len = 0
    for i in picks:
        tools_len += i * 5
    # print(tools_len,len(minerals))
    # print(tools_len < len(minerals))
    new_arr = []
    
    if tools_len <= len(minerals):
        for i in range(tools_len):
            new_arr.append(minerals[i])
    else:
         new_arr =  minerals
    
    minerals = []
    
    for i in range(0,len(new_arr),5):
        minerals.append(new_arr[i:i+5])
    
    minerals.sort( key=lambda x: (-x.count('diamond'), -x.count('iron')))
    q = deque(minerals)
    
    new_tools = deque(picks)
    
    while new_tools and q:
        tool = new_tools.popleft()
        
        while tool > 0 and q:
            tool -= 1
            mine = q.popleft()
            
            for i in mine:
                if i == 'diamond':
                    if len(new_tools) == 2 :
                        answer += 1
                    elif len(new_tools) == 1:
                        answer += 5
                    else:
                        answer += 25
                
                elif i == 'iron' :
                    if len(new_tools) == 2 or len(new_tools) == 1:
                        answer += 1
                    else:
                        answer += 5
                
                else:
                    answer += 1
                        
    return answer