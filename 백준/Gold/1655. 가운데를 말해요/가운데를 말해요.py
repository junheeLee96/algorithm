import sys
import heapq
input = sys.stdin.readline
n = int(input())

left = []
right = []

answer = []

for i in range(n):
    num = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]

        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))

    answer.append(left[0][1])

for i in answer:
    print(i)
