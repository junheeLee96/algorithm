n = list(map(str, input().strip()))

arr = [int(i) for i in n]

# print(arr)

arr.sort(reverse=True)


answer = ''.join(str(i) for i in arr)

print(answer)
