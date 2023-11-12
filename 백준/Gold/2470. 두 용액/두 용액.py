n = int(input())

arr = list(map(int, input().split()))

arr.sort()

left, right = 0, n-1

result = [arr[left], arr[right]]
answer = abs(arr[left] + arr[right])

while left < right:
    left_v = arr[left]
    right_v = arr[right]

    su = left_v + right_v

    if abs(su) < answer:
        answer = abs(su)
        result = [left_v, right_v]
        if answer == 0:
            break

    if su < 0:
        left += 1

    else:
        right -= 1


print(result[0], result[1])
