na, nb = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

dic = {}

for i in b:
    dic[i] = 1

answer = 0
arr = []

for i in a:
    if i not in dic:
        answer += 1
        arr.append(i)
print(answer)
arr.sort()
for i in arr:
    print(i, end=' ')
