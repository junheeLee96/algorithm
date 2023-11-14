n, m = map(int, input().split())

arr = list(map(int, input().split()))

max_ray_len = max(arr)
start = 1
end = sum(arr)
answer = sum(arr)
while start <= end:
    mid = (start + end) // 2
    if mid < max_ray_len:
        start = mid + 1
        continue

    log = 0
    cnt = 1

    for i in range(len(arr)):
        if log + arr[i] <= mid:
            log += arr[i]
        else:
            cnt += 1
            log = arr[i]
        # print('mid = ', mid, 'arr[i] = ', arr[i], 'log = ', log)

    if cnt <= m:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)
