import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    info = list(map(str, input().split()))
    info[0] = int(info[0])
    arr.append(info + [i])

arr.sort(key=lambda x: (x[0], x[2]))

for i in arr:
    print(i[0], i[1])
