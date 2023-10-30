import heapq

n = int(input())
heap = []
# arr = []

for _ in range(n):
    a = list(map(int, input().split()))
    for num in a:
        if len(heap) < n:
            heapq.heappush(heap, num)

        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
