n = int(input())

arr = list(map(int, input().split()))

x = int(input())

arr.sort()

left = 0
right = n - 1

cnt = 0

while left < right:
    num = arr[left] + arr[right]

    if num == x:
        cnt += 1
        left += 1

    elif num > x:
        right -= 1
    else:
        left += 1

print(cnt)
