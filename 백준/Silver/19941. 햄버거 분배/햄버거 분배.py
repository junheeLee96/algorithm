

n, k = map(int, input().split())
a = input()

arr = list(a.strip())


cnt = 0

for i in range(len(arr)):
    if arr[i] == 'P':
        for i in range(max(i - k, 0), min(i + k+1, n)):
            if arr[i] == 'H':
                arr[i] = 'z'
                cnt += 1
                break


print(cnt)
