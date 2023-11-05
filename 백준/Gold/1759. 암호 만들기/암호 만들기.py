from itertools import combinations
from collections import Counter
l, c = map(int, input().split())

arr = list(map(str, input().split()))
arr.sort()
result = []


for v in combinations(arr, l):
    c = Counter(v)
    cnt = 0
    if 'a' in c:
        cnt += 1
    if 'e' in c:
        cnt += 1
    if 'i' in c:
        cnt += 1
    if 'o' in c:
        cnt += 1
    if 'u' in c:
        cnt += 1
    if l - cnt >= 2 and cnt >= 1:
        zz = [i for i in v]
        arr.sort()
        s = ''.join(zz)
        # print(l, cnt, s)
        result.append(s)


for i in result:
    print(i)
