from collections import deque

s = []

for _ in range(4):
    s.append(deque(list(input())))

k = int(input())

r = [list(map(int, input().split())) for _ in range(k)]


def left(num, dir):
    if num < 0:
        return

    if s[num][2] != s[num+1][6]:
        left(num-1, -dir)
        s[num].rotate(dir)


def right(num, dir):
    if num > 3:
        return
    if s[num][6] != s[num-1][2]:
        right(num+1, -dir)
        s[num].rotate(dir)


for i in range(k):
    num = r[i][0] - 1
    dir = r[i][1]
    left(num-1, -dir)
    right(num + 1, -dir)
    s[num].rotate(dir)

res = 0

if s[0][0] == '1':
    res += 1

if s[1][0] == '1':
    res += 2

if s[2][0] == '1':
    res += 4

if s[3][0] == '1':
    res += 8


print(res)
