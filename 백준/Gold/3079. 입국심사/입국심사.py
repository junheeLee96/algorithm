import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(int(input()))

start = 1
end = max(arr) * m
answer = float('inf')
while start <= end:
    mid = (start + end) // 2
    temp = 0

    for i in range(n):
        temp += mid // arr[i]

    if temp >= m:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)
