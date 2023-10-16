while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break
    # (sum(a,b,c) - max(a,b,c) - min(a,b,c))은 mid값
    if sum([a, b, c]) - max([a, b, c]) <= max([a, b, c]):
        print("Invalid")
        continue

    if a == b == c:
        print('Equilateral')
        continue

    if a == b or b == c or a == c:
        print('Isosceles')
        continue

    else:
        print('Scalene')
        continue
