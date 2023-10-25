n = int(input())

arr = list(map(int, input().split()))

m = int(input())

if sum(arr) <= m:
    print(max(arr))


else:
    start = 0
    end = max(arr)

    while start <= end and start <= m:
        mid = (start + end) // 2

        log = 0

        for i in range(len(arr)):
            if arr[i] > mid:
                log += mid
            else:
                log += arr[i]

        if log <= m:
            start = mid + 1
        else:
            end = mid - 1

    print(end)
