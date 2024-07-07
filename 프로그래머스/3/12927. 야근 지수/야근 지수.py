import heapq

def solution(n, works):
    if n >= sum(works):
        return 0
    
    works = [-i for i in works]
    
    heapq.heapify(works)
    
    for _ in range(n):
        mx = heapq.heappop(works)
        mx += 1
        
        heapq.heappush(works,mx)
        
    
    return sum([i ** 2 for i in works])