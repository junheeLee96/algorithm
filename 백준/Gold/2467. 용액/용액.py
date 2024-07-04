import math


n = int(input())


arr = list(map(int, input().split()))

answer = [0, 0, math.inf]

left = 0
right = n - 1

while left < right:
    l = arr[left]
    r = arr[right]

    num = l + r
    if num == 0:
        answer = [l, r, 0]
        break

    if abs(num) < abs(answer[2]):
        answer = [l, r, num]

    if 0 > num:
        left += 1

    else:
        right -= 1


ansewr = answer[:2]

print(answer[0], answer[1])
