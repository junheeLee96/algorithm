import math

x, y = map(int, input().split())

z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    answer = math.inf  # 최솟값을 찾아야 하므로 무한대로 초기화

    start, end = 1, 1000000000  # 이분 탐색의 범위를 수정

    while start <= end:
        mid = (start + end) // 2

        new_z = ((y + mid) * 100) // (x + mid)

        if new_z <= z:
            start = mid + 1
        else:
            end = mid - 1
            answer = min(answer, mid)

    print(answer)