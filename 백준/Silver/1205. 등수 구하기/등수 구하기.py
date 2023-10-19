n, point, p = map(int, input().split())

if n <= 0:
    print(1)
else:

    arr = list(map(int, input().split()))
    rank = 1
    person = p
    for num in arr:
        if num == point:
            person -= 1
            rank = rank
        elif num < point:
            break

        elif num > point:
            person -= 1
            rank += 1

    if person <= 0:
        print(-1)
    else:
        print(rank)