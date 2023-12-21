n = int(input())

arr = list(map(int, input().split()))
arr.sort()

answer = 0

for i in range(n):
    temp = arr[:i] + arr[i+1:]

    left = 0
    right = len(temp) - 1

    while left < right:
        num = temp[left] + temp[right]

        if num == arr[i]:
            answer += 1
            break
        elif num > arr[i]:
            right -= 1
        else:
            left += 1

print(answer)
