

x, y = map(int, input().split())

origin_ = (y * 100) // x


if origin_ >= 99:
    print(-1)
else:
    answer = float('inf')
    start = 1
    end = 1000000000

    while start <= end:
        mid = (start + end) // 2
        l = ((y + mid) * 100) // (x + mid)
        # print(mid, l)

        if l > origin_:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    print(answer)
