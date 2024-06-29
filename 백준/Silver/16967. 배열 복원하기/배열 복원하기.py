h, w, x, y = map(int, input().split())


arr = []

for _ in range(h+x):
    arr.append(list(map(int, input().split())))

a = [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        a[i][j] = arr[i][j]


for i in range(h):
    for j in range(w):
        if x + i < h and j + y < w:
            a[i+x][j+y] -= a[i][j]


for i in a:
    print(' '.join(map(str, i)))