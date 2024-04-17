def solution(brown, yellow):
    answer = []
    
    total = brown + yellow
    
    for i in range(2,total):
        if total % i == 0:
            width = i
            
            height = total // width
            
            if width >= height and 2*width + 2*height == brown + 4:
                answer = [width,height]
            
    return answer




# def solution(brown, yellow):
#     answer = []
#     total = brown + yellow
#     for width in range(1,total):
#         if total % width == 0:
#             height = total // width
#             if width >= height and 2*width + 2*height == brown + 4:
#                 return [width,height]
#     return answer
