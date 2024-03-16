
import heapq
import math
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
INF = math.inf
arr = [[] for _ in range(n+1)]

start = int(input())
visit = [False for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())

    arr[a].append((b, c))


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


dj(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
