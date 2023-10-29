p, m = map(int, input().split())

arr = []

for _ in range(p):
    lev, name = map(str, input().split())
    lev = int(lev)
    is_Join = False

    for i in range(len(arr)):
        if arr[i][0][0] - 10 <= lev <= arr[i][0][0]+10:
            if len(arr[i]) <= m-1:
                arr[i].append([lev, name])
                is_Join = True
                break
            # arr[i].append([lev, name])
            # is_Join = True

            # if len(arr[i]) >= m:
            #     print('Started!')
            #     room = arr.pop(i)
            #     room.sort(key=lambda x: (x[1]))
            #     for k in room:
            #         print(k[0], k[1])
            #         # print(room[k][0], room[k][1])
            #     break

    if is_Join == False:
        arr.append([[lev, name]])

for room in arr:
    if len(room) >= m:
        print('Started!')
        room.sort(key=lambda x: x[1])

        for userinfo in room:
            print(userinfo[0], userinfo[1])
    else:
        print('Waiting!')

        room.sort(key=lambda x: x[1])
        for userinfo in room:
            print(userinfo[0], userinfo[1])