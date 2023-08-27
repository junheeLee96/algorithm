import math

X, Y = map(int, input().split())


Z = (Y * 100) // X

if Z >= 99:
    print(-1)
else:

    right = X
    left = 1

    answer = 0

    while left <= right:

        mid = (left + right) // 2

        if (Y + mid) * 100 // (X + mid) <= Z:
            left = mid+1
        else:
            answer = mid
            right = mid - 1

    print(answer)
