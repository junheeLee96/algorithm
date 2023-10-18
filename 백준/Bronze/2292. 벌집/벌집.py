n = int(input())

if n == 1:
    print(1)
else:

    max_n = 1000000000

    loop = max_n // 6

    # dp = [7]
    cnt = 1
    m = 2
    for i in range(1, n):
        cnt += (6 * i)

        if n <= cnt:
            print(m)
            break
        else:
            m += 1
