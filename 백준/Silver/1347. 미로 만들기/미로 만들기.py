n = int(input())

s = input()

arr = [[0, 0]]

# 동 남 서 북 0,1,2,3

x, y, d = 0, 0, 1

for i in s:
    if i == 'R':
        d = (d + 1) % 4
    elif i == 'L':
        d = (d - 1) % 4

    else:
        if d == 0:
            # 동
            x = x
            y += 1

        elif d == 1:
            x += 1
            y = y

        elif d == 2:
            x = x
            y -= 1

        else:
            x -= 1
            y = y

        arr.append([x, y])

min_x = 0
min_y = 0

max_x = 0
max_y = 0

for i in arr:
    x, y = i[0], i[1]
    min_x = min(x, min_x)
    min_y = min(y, min_y)

    max_x = max(x, max_x)
    max_y = max(y, max_y)


n = (max_x - min_x) + 1
m = (max_y - min_y) + 1

for i in arr:
    i[0] = i[0] + abs(min_x)
    i[1] += abs(min_y)

g = [['#' for _ in range(m)] for _ in range(n)]

for i in arr:
    nx, ny = i[0], i[1]
    g[nx][ny] = '.'

for i in g:
    for j in i:
        print(j, end='')
    print()

# graph = [['#' for _ in range(m)] for _ in range(n)]
