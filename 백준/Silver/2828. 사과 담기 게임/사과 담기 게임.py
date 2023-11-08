n, m = map(int, input().split())

j = int(input())

left = 1
right = m
cnt = 0

for _ in range(j):
    position = int(input())

    if left > position:
        # 사과과 바구니보다 왼쪽에서 떨어지면
        cnt += (left - position)
        # 사과가 바구니 가장 왼쪽에 오게 설정
        left = position
        right = left + m - 1

    elif right < position:
        cnt += position - right
        right = position
        left = right - m+1

print(cnt)
