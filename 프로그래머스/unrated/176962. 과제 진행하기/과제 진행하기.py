from collections import deque


def solution(plans):
    answer = []
    q = deque()

    for i in range(len(plans)):
        #         시간을 분으로 변환 = 시간 * 60 + 분
        time = plans[i][1].split(':')
        new_time = int(time[0]) * 60 + int(time[1])
        plans[i][1] = new_time

    plans = sorted(plans, key=lambda x: x[1])
#     시간 순으로 정렬
    print(plans)

    for i in range(0, len(plans)-1):

        work = plans[i]
        next_work = plans[i+1]

        done_time = int(work[1]) + int(work[2])
        diff_time = next_work[1] - done_time

        if diff_time < 0:
            left_hour = abs(diff_time)
            work[2] = left_hour
            q.append(work)

        else:
            answer.append(work[0])
            if q:
                while diff_time > 0 and q:
                    left_work = q.pop()
                    diff_time -= left_work[2]

                    if diff_time < 0:
                        left_work[2] = abs(diff_time)
                        q.append(left_work)
                    elif diff_time == 0:
                        answer.append(left_work[0])

                    else:
                        answer.append(left_work[0])
        if i == len(plans) - 2:
            answer.append(plans[i+1][0])
            while q:
                q_work = q.pop()
                answer.append(q_work[0])

    # while q or plans:

    #     if len(plans) >= 2:
    #         work = plans.pop(0)
    #         next_work = plans[0]
    #         work_done_time = int(work[1]) + int(work[2])

    #         time_difference = int(next_work[1]) - work_done_time
    #         if time_difference > 0:
    #             answer.append(work[0])
    #             if q:
    #                 while time_difference:
    #                     keep_work = q.pop()
    #                     time_difference -= keep_work[2]
    #                     if time_difference < 0:
    #                         keep_work[2] = abs(time_difference)
    #                         q.append(keep_work)
    #                     else:
    #                         print('------')
    #                         print('plans.length > 1')
    #                         print('if q')
    #                         print('time_difference > 0')
    #                         print(time_difference)
    #                         print(keep_work)
    #                         answer.append(keep_work[0])
    #         elif time_difference == 0:
    #             answer.append(work[0])
    #         else:
    #             work[2] = abs(time_difference)
    #             q.append(work)

    #     elif len(plans) == 1:
    #         work = plans.pop(0)
    #         print('------')
    #         print('plans.length == 1')
    #         print(work)
    #         answer.append(work[0])

    #     else:
    #         while q:
    #             work = q.pop()
    #             print('------')
    #             print('else while q')
    #             print(work)
    #             answer.append(work[0])
    #     print('----')
    #     print(q)

    return answer

