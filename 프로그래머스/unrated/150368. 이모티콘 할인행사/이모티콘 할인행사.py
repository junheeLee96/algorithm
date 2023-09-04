from itertools import product


def solution(users, emoticons):
    answer = [0,0]
    sales = [10, 20, 30, 40]    # 이모티콘의 할인율


    for case in product(sales, repeat=len(emoticons)):
        plus = 0
        money = 0
        for user in users:
            total = 0
            for idx, sale in enumerate(case):
                if case[idx] >= user[0]:
                    total += emoticons[idx] * (100 - sale) // 100 
                    
            if user[1] <= total:
                plus += 1
            else:
                money += total
        if answer[0] < plus:
            answer[0] = plus
            answer[1] = money
        elif answer[0] == plus:
            if answer[1] < money:
                answer[1] = money

    return answer