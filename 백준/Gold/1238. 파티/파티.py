import sys
import math
import heapq

input = sys.stdin.readline
INF = math.inf

n, m, x = map(int, input().split())

arr = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    arr[a].append((b, c))


def dj(start):
    distance = [INF] * (n+1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if now == x and start != x:
            return distance

        if dist > distance[now]:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


ans = [0 for _ in range(n+1)]

for i in range(1, n+1):
    lst = dj(i)

    # print(arr[i])
    # print(i, lst)
    if x != i:
        ans[i] += lst[x]
    else:
        for idx in range(1, n+1):
            if idx != x:
                ans[idx] += lst[idx]

print(max(ans))
