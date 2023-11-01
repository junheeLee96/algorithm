
n = int(input())

arr = [0, 1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16]

for i in range(12, 100001):
    # arr.append()
    # a = arr[i]
    arr.append(arr[i-6] + i)
for i in range(n):
    num = int(input())
    print(arr[num])