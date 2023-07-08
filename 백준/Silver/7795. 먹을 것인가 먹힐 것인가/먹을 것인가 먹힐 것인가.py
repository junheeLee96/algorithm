def binary_search(ls: list, x: int) -> int:
    start = 0
    end = len(ls) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if ls[mid] < x:
            start = mid
        elif ls[mid] >= x:
            end = mid

    if x <= ls[start]:
        return 0
    elif ls[start] < x <= ls[end]:
        return end
    else:
        return len(ls)


t = int(input())
for tc in range(t):
    a_length, b_length = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        tmp = binary_search(B, a)
        cnt += tmp
    print(cnt)
