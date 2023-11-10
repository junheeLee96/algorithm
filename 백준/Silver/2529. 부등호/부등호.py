def get_num(x, y, oper):
    if oper == '<':
        if x > y : 
            return False 
    else:
        if x < y:
            return False 
    return True 

def dfs(idx, num):
    if idx == k+1:
        ans.append(num)
        return

    for i in range(10):
        if not check[i]:
            if idx == 0 or get_num(num[idx-1], str(i), oper[idx-1]):
                check[i] = True 
                dfs(idx + 1, num + str(i))
                check[i] = False 

k = int(input())
oper = list(input().split())

check = [False] * 10
ans = []
dfs(0, '')

ans.sort()
print(ans[-1])
print(ans[0])