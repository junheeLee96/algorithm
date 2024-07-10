import heapq

def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    arr = []
    for i in B:
        heapq.heappush(arr,-i)
    
    for a in A:
        num = heapq.heappop(arr)
        if -num > a:
            answer += 1
        else:
            heapq.heappush(arr,num)
    
#     for a in A:
#         idx = 0
        
#         while idx < len(B):
#             if a < B[idx]:
#                 answer += 1
#                 B.remove(B[idx])
#                 break
#             idx += 1
        # for i in range(len(B)):
        #     if a < B[i]:
        #         answer += 1
        #         B.remove(B[i])
        #         break
                
                
            
        
    return answer




# from bisect import bisect_left

# def solution(A, B):
#     answer = 0
#     B.sort()
#     A.sort(reverse=True)
#     for i in A:
#         # print('--------')
#         idx = bisect_left(B, i)
#         # print('idx = ', idx)
#         # print('B = ', B)
#         if idx > len(B) - 1:
#             continue
#         if i < B[idx]:
#             answer += 1
#             B.pop(idx)
#     # print(answer)
#     return answer