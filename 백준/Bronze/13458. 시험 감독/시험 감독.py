n = int(input())

arr = list(map(int, input().split()))

a, b = map(int, input().split())

cnt = 0

for i in range(n):
    if arr[i] <= a:
        cnt += 1
    else:
        arr[i] -= a

        cnt += 1

        if arr[i] % b == 0:
            cnt = cnt + (arr[i] // b)
        else:
            cnt = cnt + (arr[i] // b) + 1

print(cnt)
