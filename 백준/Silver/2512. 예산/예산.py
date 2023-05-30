n = int(input())

arr = list(map(int, input().split()))
money = int(input())

start = 0
end = max(arr)

max_log = 0

if sum(arr) <= money:
    print(max(arr))

else:
    while start <= end and start <= money:
        mid = (start + end) // 2

        log = 0
        for i in arr:
            if i > mid:
                log += mid
            else:
                log += i
        if log <= money:
            if max_log < log:
                max_log = log
            start = mid + 1
        else:
            end = mid - 1

    print(end)
# print(max_log)
