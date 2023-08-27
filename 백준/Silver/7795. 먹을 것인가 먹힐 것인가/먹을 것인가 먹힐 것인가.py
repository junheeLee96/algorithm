from bisect import bisect_left

t = int(input())

answer = []

for i in range(t):
    n, m = map(int, input().split())

    cnt = 0

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    for num in a:
        idx = bisect_left(b, num)

        cnt += idx

    answer.append(cnt)

for i in answer:
    print(i)
