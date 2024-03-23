def solution(friends, gifts):
    f_dic = {}
    sum_dic = {}
    answer = 0

    # for

    for i in range(len(friends)):
        f_dic[friends[i]] = {}
        sum_dic[friends[i]] = [0, 0]
        for j in range(len(friends)):
            if i == j:
                continue
            f_dic[friends[i]][friends[j]] = 0

    # print(f_dic)
    dic = {}

    for i in range(len(gifts)):
        a = gifts[i].split()
        send, receive = a[0], a[1]
        f_dic[send][receive] += 1

        if send not in sum_dic:
            sum_dic[send] = [1, 0]
        else:
            sum_dic[send][0] += 1

        if receive not in sum_dic:
            sum_dic[receive] = [0, 1]
        else:
            sum_dic[receive][1] += 1

    # print(sum_dic)
    # return 0

    for key_1, value_1 in f_dic.items():
        # a = sorted(value_1.values(), key=lambda x: x)
        # if max(a) == 0:
        #     continue

        dic[key_1] = 0
        for key_2, value_2 in value_1.items():
            key_2_to_key_1 = f_dic[key_2][key_1]
            if value_2 > key_2_to_key_1:
                dic[key_1] += 1
            elif key_2_to_key_1 > value_2:
                continue
            elif key_2_to_key_1 == value_2 or value_2 == 0:
                if key_2 not in sum_dic:
                    continue
                elif key_1 not in sum_dic:
                    continue
                s_1 = sum_dic[key_1][0] - sum_dic[key_1][1]
                s_2 = sum_dic[key_2][0] - sum_dic[key_2][1]

                if s_1 > s_2:
                    dic[key_1] += 1

    answer = max(sorted(dic.values(), key=lambda x: x))
    return answer