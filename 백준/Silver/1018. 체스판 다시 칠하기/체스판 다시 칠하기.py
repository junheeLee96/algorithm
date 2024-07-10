import math

answer = []

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(str, input().strip())))


for i in range(n - 7):
    for j in range(m - 7):
        a = 0
        b = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):

                if (x+y) % 2 == 0:
                    if arr[x][y] != 'B':
                        a += 1
                    if arr[x][y] != 'W':
                        b += 1

                else:
                    if arr[x][y] != 'W':
                        a += 1
                    if arr[x][y] != 'B':
                        b += 1

        answer.append(a)
        answer.append(b)

        # if arr[x][y-1] == arr[x][y]:
        #     cnt += 1

        # answer = min(answer, cnt)


print(min(answer))
