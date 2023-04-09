def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    arr = [0] * bridge_length
    
    while arr:
        answer += 1
        
        arr.pop(0)
        if truck_weights:
            if sum(arr) + truck_weights[0] <= weight:
                arr.append(truck_weights.pop(0))
            else:
                arr.append(0)
    return answer