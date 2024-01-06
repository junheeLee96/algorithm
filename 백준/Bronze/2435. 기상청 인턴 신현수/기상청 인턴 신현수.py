n, k = map(int, input().split())

arr = list(map(int, input().split()))

num = sum(arr[:k])

answer = num

idx = 0
# print('num = ', num)

for i in range(k-1, n-1):
    num = num - arr[idx] + arr[i+1]
    answer = max(answer, num)
    idx += 1

print(answer)
