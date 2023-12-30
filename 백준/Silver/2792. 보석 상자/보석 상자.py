n, m = map(int, input().split())

arr = []

for _ in range(m):
    arr.append(int(input()))

start = 1
end = sum(arr)

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for i in arr:
        if i % mid == 0:
            temp = temp + i // mid
        else:
            temp = temp + (i // mid) + 1

    if temp > n:
        start = mid+1
    else:
        end = mid - 1

print(start)
