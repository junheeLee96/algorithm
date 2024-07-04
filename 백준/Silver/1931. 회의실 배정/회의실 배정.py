import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x: (x[1], x[0]))

cnt = 0
prev_time = 0  # 마지막으로 회의 끝난 시간

for i in arr:
    if prev_time <= i[0]:
        cnt += 1

        prev_time = i[1]
print(cnt)
