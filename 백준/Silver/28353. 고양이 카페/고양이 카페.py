n, k = map(int, input().split())

arr = list(map(int, input().split()))


arr.sort()
cnt = 0
start = 0
end = n-1

while start < end:
    cat_1 = arr[start]
    cat_2 = arr[end]

    if cat_1 + cat_2 <= k:
        cnt += 1
        end -= 1
        start += 1
    elif cat_1 + cat_2 > k:
        end -= 1

print(cnt)
