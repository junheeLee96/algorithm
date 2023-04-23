a,l = map(int,input().split())


arr = list(map(int,input().split()))
arr.sort()

answer =1

last = (arr[0] - 1) + l

for i in range(1,len(arr)):
    if arr[i] <= last:
        continue
    else:
        answer += 1
        last = (arr[i]-1) + l

print(answer)