from copy import deepcopy
from collections import Counter

n = int(input())
answer = 0
arr = []

for i in range(n):
    s = input()

    if i == 0:
        for j in s:
            arr.append(j)
    else:
        cop = deepcopy(arr)

        new = [j for j in s]
        cnt = 0
        for j in new:
            if j in cop:
                cop.remove(j)
            else:
                cnt += 1
        if cnt < 2 and len(cop) < 2:
            answer += 1

print(answer)