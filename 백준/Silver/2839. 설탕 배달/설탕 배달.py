n = int(input())
if n % 5 == 0:
    print(n // 5)
else:
    cnt = 0

    while n > 0:
        n -= 3
        cnt += 1

        if n % 5 == 0:
            cnt += n // 5
            break
        if n == 1 or n == 2:
            cnt = -1
            break

    print(cnt)
