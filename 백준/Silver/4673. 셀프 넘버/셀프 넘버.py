def d(n):
    new_n = n
    for i in str(n):
        new_n += int(i)

    return new_n


arr = [i for i in range(1, 10001)]

for i in range(1, 10001):
    not_s = d(i)

    if not_s in arr:
        arr.remove(not_s)

for i in arr:
    print(i)
