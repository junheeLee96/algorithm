n = int(input())

arr = []

end = 0
start = 0
s = 0

for _ in range(n):
    l = list(map(int, input().split()))

    for m in l:
        arr.append(m)
        end = max(end, m)
        s += m

s = s / 2

answer = float('inf')

while start <= end:
    mid = (start + end) // 2
    temp = 0

    for number in arr:
        if number >= mid:
            temp += mid
        else:
            temp += number

    if temp >= s:
        answer = min(mid, answer)
        end = mid - 1

    else:
        start = mid + 1


print(answer)
