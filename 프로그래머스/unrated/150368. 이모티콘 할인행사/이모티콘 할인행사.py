from itertools import product


def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]    # 이모티콘의 할인율

    answer = []

    sales = [10, 20, 30, 40]

    for case in product(sales, repeat=len(emoticons)):
        result = [0, 0]

        for user in users:
            temp = 0

            for idx, sale in enumerate(case):
                if sale >= user[0]:
                    temp += emoticons[idx] * (100 - sale) // 100

            if temp >= user[1]:
                result[0] += 1
            else:
                result[1] += temp

        answer.append(result)

    answer.sort(key=lambda x: (-x[0], -x[1]))

    return answer[0]