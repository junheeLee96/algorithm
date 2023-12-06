n, m = map(int, input().split())

dic = {}

arr = []
arr2 = []
for _ in range(n):
    arr.append(input())

for _ in range(m):
    arr2.append(input())

inter = list(set(arr) & set(arr2))

print(len(inter))
inter.sort()
for i in inter:
    print(i)
