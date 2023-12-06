n, m = map(int, input().split())

dic = {}

arr = []

for i in range(n):
    s = input()

    dic[s] = i

for i in range(m):
    s = input()

    if s in dic:
        arr.append(s)


arr.sort()
print(len(arr))
for i in arr:
    print(i)
