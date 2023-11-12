import sys

# 장애물의 개수와 전체 높이
n, h = map(int, sys.stdin.readline().split())

# 석순 정보 저장
down = [0] * (h+1)
# 종유석 정보 저장
up = [0] * (h+1)

# 장애물의 크기 입력
for i in range(n):

    height = int(sys.stdin.readline())

    if (i % 2 == 0):
        # 석순의 높이에 따라 1 증가
        down[height] += 1
    else:
        # 종유석의 높이에 따라 1 증가
        up[height] += 1

# 인덱스를 역순으로 누적합을 계산
for i in range(h-1, 0, -1):
    down[i] += down[i+1]
    up[i] += up[i+1]

# 최소로 잘리는 장애물의 개수
min_count = n

# 동일한 개수로 잘리는 높이의 수
same_height = 0

# 전체 높이 i 기준, 높이에 따라 잘리는 석순과 종유석의 개수 파악
for i in range(1, h+1):

    # 현재까지 최소로 잘린 개수보다 현재 높이에서 더 적은 수로 잘리는 경우
    if (min_count > down[i] + up[h - i + 1]):
        min_count = down[i] + up[h - i + 1]
        same_height = 1

    # 현재 높이에서 잘린 개수가 현재까지 최소로 잘린 개수와 동일하다면
    elif (min_count == down[i] + up[h - i + 1]):
        same_height += 1

print(min_count, same_height)