n = int(input())

arr = list(map(int, input().split()))

answer = [0 for _ in range(n)]

for i in range(n):
    cnt = 0
    for j in range(n):
        if answer[j] == 0 and cnt == arr[i]:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1
print(' '.join(map(str, answer)))
