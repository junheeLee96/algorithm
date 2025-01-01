def solution(wallet, bill):
    answer = 0
    if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
        return 0
    
    while max(bill) > max(wallet) or min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] = bill[0] // 2
            answer += 1
        elif bill[1] > bill[0]:
            bill[1] = bill[1] // 2
            answer += 1
            
        if bill[0] <= wallet[0] and bill[1] <= wallet[1]:
            return answer
        if bill[0] <= wallet[1] and bill[1] <= wallet[0]:
            return answer
        
    return answer