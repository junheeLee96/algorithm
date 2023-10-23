n = int(input())

arr = list(map(int, input().split()))

arr = [-1] + arr

m = int(input())

stu = []


def male(num):
    for i in range(1, n+1):
        if i % num == 0:
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1


def female(num):
    if arr[num] == 1:
        arr[num] = 0
    else:
        arr[num] = 1

    left = num - 1
    right = num + 1

    while left > 0 and right <= n:
        if arr[left] == arr[right]:
            if arr[left] == 1:
                arr[left] = 0
                arr[right] = 0
            else:
                arr[left] = 1
                arr[right] = 1

            left -= 1
            right += 1
        else:
            break


for i in range(m):
    sex, num = map(int, input().split())

    if sex == 1:
        male(num)
    else:
        female(num)


for i in range(1, len(arr)):
    if i > 0 and i % 20 == 0:
        print(arr[i])
    else:
        print(arr[i], end=' ')
