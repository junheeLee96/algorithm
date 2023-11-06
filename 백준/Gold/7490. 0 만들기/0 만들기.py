# t = int(input())

# result = []


# def dfs(arr, current_idx, n, s, condition, num):
#     if current_idx == n:
#         new_s = s.replace(' ', '')

#         if eval(new_s) == 0:
#             if s not in result:
#                 result.append(s)
#         return

#     if condition == 'plus':
#         s = s + '+' + str(arr[current_idx])
#     elif condition == 'minus':
#         s = s + '-' + str(arr[current_idx])
#     else:
#         s = s + ' ' + str(arr[current_idx])

#     current_idx += 1

#     dfs(arr, current_idx, n, s, 'plus', num)
#     dfs(arr, current_idx, n, s, 'minus', num)
#     dfs(arr, current_idx, n, s, 'space', num)


# for _ in range(t):
#     n = int(input())
#     result = []

#     arr = [i+1 for i in range(n)]

#     dfs(arr, 1, n, '1', 'plus', 1)
#     dfs(arr, 1, n, '1', 'minus', 1)
#     dfs(arr, 1, n, '1', 'space', 1)
#     result.sort()
#     print(result)
t = int(input())

result = []


def dfs(n, s, num):
    if num == n:
        if eval(s.replace(' ', '')) == 0:
            return print(s)
        return
    num += 1

    dfs(n, s+' '+str(num), num)
    dfs(n, s+'+'+str(num), num)
    dfs(n, s+'-'+str(num), num)


for _ in range(t):
    n = int(input())

    dfs(n, '1', 1)
    print()
