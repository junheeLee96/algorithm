from collections import defaultdict


def calculate_10_percent(x):
    y = x * 0.1  # x의 10% 계산
    return int(y) if y >= 1 else 0


def solution(enroll, referral, seller, amount):
    answer = []
    obj = {}
#     idea
# 일단 obj를 만든다. obj는
# obj['이름'] = {ref:내가 참여시킨 놈, enr: 날 참가하게 해준놈}

    count = defaultdict(int)

    def dfs(current, money,i):
        percent_10 = calculate_10_percent(money)
        parent = obj[current]
        if (i == 0):
            print(current,parent,money,percent_10, money-percent_10)
        if parent == '-':
            count[current] += money-percent_10
            return

        
        if percent_10 == 0:
            count[current] += money
            return
        else:
            count[current] += money-percent_10
            dfs(parent, percent_10,i)

    for i in range(len(enroll)):
        a = referral[i]  # 나를 가입시킨 놈
        b = enroll[i]  # 나
        obj[b] = a

    for i in range(len(seller)):
        money = amount[i] * 100
        sell = seller[i]

        dfs(sell, money,i)

    for i in range(len(enroll)):
        answer.append(count[enroll[i]])

    return answer