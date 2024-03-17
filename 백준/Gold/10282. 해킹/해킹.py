import heapq
import sys
import math

input = sys.stdin.readline
INF = math.inf

t = int(input())


for _ in range(t):
    n, d, start = map(int, input().split())

    arr = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        arr[b].append((a, s))
    distance = [INF] * (n+1)
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    cnt = 0
    time = 0
    for i in distance:
        if i != INF:
            time = max(time, i)
            cnt += 1
    print(cnt, time)
