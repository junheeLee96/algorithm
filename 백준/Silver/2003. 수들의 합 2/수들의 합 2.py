n, m = map(int, input().split())

arr = list(map(int, input().split()))


start = 0
end = 1

cnt = 0


while start <= end and end <= n:
    number = sum(arr[start:end])
    if number == m:
        cnt += 1
        end += 1
    elif number > m:
        start += 1
    else:
        end += 1

print(cnt)
