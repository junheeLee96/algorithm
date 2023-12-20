# def solution(nums):
#     dic = {}
    
#     for i in nums:
#         if i not in dic:
#             dic[i] = 1
#         else:
#             dic[i] += 1
#     m = len(nums) // 2
    
#     for i in range(len(dic)):
#         print(i)
    








def solution(nums):
    answer = 0
    a = {}
    for i in range(len(nums)):
        s = str(nums[i])
        a[s] = 0
    number = len(nums) //2
    
    for i in range(len(a)):
        if i+1 <= len(nums)//2:
            # print(i)
            answer+=1
    return answer