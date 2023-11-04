arr = []

n, m = map(int, input().split())

for i in range(n):
    s = input()

    a = [i for i in s]
    arr.append(a)


width = min(n, m)


def check(s):
    for i in range(n-s + 1):
        for j in range(m - s + 1):
            if arr[i][j] == arr[i][s + j - 1] == arr[i + s - 1][j] == arr[i + s - 1][j+s-1]:
                return True

    return False


for i in range(width, 0, -1):
    if check(i):
        print(i ** 2)
        break
