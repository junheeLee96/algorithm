n = int(input())

arr = set()

for _ in range(n):
    arr.add(input())

arr = list(arr)

arr.sort()

arr.sort(key=lambda x: len(x))

for i in arr:
    print(i)
