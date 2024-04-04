import math

INF = math.inf

n = int(input())

arr = list(map(int, input()))

target = list(map(int, input()))


def func(a, b):
    l = a[:]

    cnt = 0
    for i in range(1, n):
        if l[i-1] == target[i-1]:
            continue
        cnt += 1

        for j in range(i-1, i+2):
            if j < n:
                l[j] = 1 - l[j]

    return cnt if l == b else INF


ans = func(arr, target)

arr[0] = 1 - arr[0]
arr[1] = 1 - arr[1]

answer = min(ans, func(arr, target) + 1)
if answer == INF:
    print(-1)
else:
    print(answer)
