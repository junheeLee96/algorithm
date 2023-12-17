dic = {}

s = str(input())

for i in range(10):
    dic[i] = 0

for i in s:
    if i == '6' or i == '9':
        if dic[6] >= dic[9]:
            dic[9] += 1
        else:
            dic[6] += 1

    # if i == '6':
    #     if dic['6'] >= dic['9']:
    #         dic['9'] += 1
    #     else:
    #         dic['6'] += 1

    # elif i == '9':
    #     if dic['9'] >= dic['6']:
    #         dic['6'] += 1
    #     else:
    #         dic['9'] += 1

    else:
        dic[int(i)] += 1

cnt = 0

for value in dic.values():
    cnt = max(cnt, value)

print(cnt)
