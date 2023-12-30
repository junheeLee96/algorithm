n, m = map(int, input().split())

arr = list(map(int, input().split()))

start = 1
end = max(arr)

answer = 0

while start <= end:
    mid = (start + end) // 2

    temp = 0

    for num in arr:
        temp += num // mid

    if temp >= n:
        answer = max(mid, answer)
        start = mid + 1
    else:
        end = mid - 1

print(answer)
