import math
import heapq
import sys
input = sys.stdin.readline

INF = math.inf

n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())

    arr[a].append((b, c))
    arr[b].append((a, c))


def dj(start):
    q = []

    heapq.heappush(q, (0, start))

    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in arr[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dj(1)

print(distance[n])
