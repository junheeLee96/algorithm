n, kim, im = map(int, input().split())

if n % 2 == 1:
    n += 1

if kim % 2 == 1:
    kim += 1

if im % 2 == 1:
    im += 1


cnt = 1

while True:
    if kim % 2 == 1:
        kim += 1

    if im % 2 == 1:
        im += 1
    if kim // 2 == im // 2:
        # print(kim, im)
        break

    kim = kim // 2
    # 8 4 2 1
    im = im // 2
    #  9 5 3 2
    cnt += 1


print(cnt)
