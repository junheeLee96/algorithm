
s = 0
m = 99999999

for _ in range(7):
    num = int(input())

    if num % 2 == 0:
        continue

    s += num

    if m > num:
        m = num

if s == 0:
    print(-1)
else:
    print(s)
    print(m)
