import heapq
import math


INF = math.inf


def dj(start):
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


n, d = map(int, input().split())

arr = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    arr[i].append((i+1, 1))


for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    arr[a].append((b, c))

dj(0)

print(distance[d])
