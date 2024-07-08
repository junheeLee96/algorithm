def solution(sequence, k):
    partial_sum = 0
    right = 0
    result = []
    for left in range(len(sequence)):
        while right < len(sequence) and partial_sum < k:
            partial_sum += sequence[right]
            right += 1

        if partial_sum == k:
            if not result:
                result = [left, right - 1]
                print(left)
            else:
                if result[1] - result[0] <= (right - 1) - left:
                    result = result    
                else :
                    result = [left, right - 1]

        partial_sum -= sequence[left]
    return result