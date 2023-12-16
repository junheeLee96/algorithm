n = int(input())

arr = [[0 for _ in range(101)] for _ in range(101)]

cnt = 0

# print('-------')
for i in range(n):
    x, y = map(int, input().split())
    area = 100
    position = [[y + 10, x], [y+10, x+10], [y, x+10], [y, x]]

    # for sq in arr:
    #     if sq[0][0]

    for j in range(y, y+10):
        for k in range(x, x+10):
            arr[j][k] = 1


cnt = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
