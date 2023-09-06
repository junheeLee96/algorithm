from itertools import product as cb


def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))

    while storey:
        floor = storey.pop()
        if (floor == 5 and ((storey and storey[-1] < 5) or not storey)) or floor < 5:
            answer += floor
        else:
            answer += (10 - floor)
            if(storey):
                storey.append(storey.pop() + 1)
            else:
                answer += 1

    return answer