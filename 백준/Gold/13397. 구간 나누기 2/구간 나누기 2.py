n, m = map(int, input().split())

arr = list(map(int, input().split()))

l = 0
r = max(arr)

result = r
while l <= r:
    mid = (l + r) // 2

    low = arr[0]
    high = arr[0]
    d = 1

    for i in arr:
        if high < i:
            high = i

        if low > i:
            low = i

        if high - low > mid:
            d += 1
            low = i
            high = i
    if (m >= d):
        r = mid - 1
        result = min(result, mid)
    else:
        l = mid + 1
print(result)
