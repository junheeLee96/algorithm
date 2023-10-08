import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))


# 순서를 유지해야 하므로 정렬을 사용하면 안된다.
# 이분탐색을 두번 적용 시켜서
num = sum(data)

start = 0  # num // 3
end = 10000000000
result = num

while start <= end:
    # mid 는 블루레이 크기
    mid = (start+end) // 2
    if mid < max(data):
        start = mid + 1
        continue
    # cnt 는 블루레이 개수 , tmp 는 블루레이 갱신해주고 있는 블루레이 길이
    cnt, tmp = 1, 0
    # 하나씩 더하면서 갱신해준다.
    for i in range(len(data)):
        # 이전 값이랑 지금 값 더해서 mid 보다 작으면 계속 더해준다
        if tmp + data[i] <= mid:
            tmp += data[i]
        # mid 보다 커지면 현재 data[i]가 tmp 로 들어가고
        # 전에 있던 tmp는 0 초기화 해주고 개수 1개 늘려준다.
        else:
            tmp = data[i]
            cnt += 1
    # 개수가 m-1보다 작거나 같으면 이분탐색으로 영상 길이 인 mid값 갱신 로직 실행ㄴ
    if cnt <= m:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1
print(result)
