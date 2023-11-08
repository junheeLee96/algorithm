n, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
for i in arr:
    if i <= l:
        l += 1

print(l)
