arr = [int(input()) for _ in range(10)]


temp = 0

for i in range(10):
    num = temp + arr[i]

    if num >= 100:
        if abs(100 - num) == abs(100 - temp):
            temp = num
            break
        if abs(100 - num) < abs(100 - temp):
            temp = num
            break
        break
    else:
        temp = num

print(temp)
