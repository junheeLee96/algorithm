n, k = map(int, input().split())
k -= 1
init_k = k

arr = [i for i in range(1, n+1)]
answer = []
# print(n, k)
while n > 1:
    answer.append(arr.pop(k))
    n = len(arr)
    k += init_k
    # print(arr, answer, n, k)
    if k >= n:
        while k >= n:
            k = k - n
    # print(n, k)
# arr = [1, 2, 3]

# arr = arr * 3

# print(arr)

# print(answer+[arr[0]])
answer += [arr[0]]

s = '<'

for i in range(len(answer)):
    # print(i, len(answer))
    if i == len(answer)-1:
        s += str(answer[i])
    else:
        s += str(answer[i]) + ', '


s += '>'
print(s)
