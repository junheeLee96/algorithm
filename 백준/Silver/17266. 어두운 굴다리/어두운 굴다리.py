N = int(input())
M = int(input())

positions = list(map(int, input().split()))
len_positions = len(positions)

min_height = 0

# 가로등이 하나 있는 경우
if len_positions == 1:
    min_height = max(positions[0] - 0, N - positions[0])
# 가로등이 하나 이상인 경우
else:
    for i in range(len_positions):
        # 입구 근처의 첫번째 가로등이 비춰줘야할 거리
        if i == 0:
            height = positions[i] - 0
        # 끝나는 지점 기준 가장 가까운 가로등이 비춰줘야할 거리
        elif i == len_positions - 1:
            height = N - positions[i]
        # 양 끝의 가로등을 제외한 가로등
        else:
            tmp = positions[i] - positions[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        # 가장 큰 범위를 찾으면 되니까 max로 갱신
        min_height = max(height, min_height)

print(min_height)