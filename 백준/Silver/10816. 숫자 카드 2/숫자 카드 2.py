from collections import Counter

n = int(input())

arr = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))


dic = Counter(arr)

for i in arr2:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')
