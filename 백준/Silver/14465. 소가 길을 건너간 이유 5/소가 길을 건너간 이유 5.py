n, k, b = map(int, input().split())

arr = [i for i in range(1, n+1)]


for _ in range(b):
    arr[int(input())-1] = -1

answer = 0

for i in range(k):
    if arr[i] == -1:
        answer += 1
temp = answer

for i in range(1, n-k+1):
    if arr[i-1] == -1:
        temp -= 1
    if arr[i+k-1] == -1:
        temp += 1

    answer = min(answer, temp)
print(answer)
