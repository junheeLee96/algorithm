from collections import deque

n = int(input())

arr = deque([i+1 for i in range(n)])

z = True

answer = []

while len(arr) > 0:
    if z == True:
        answer.append(arr.popleft())
        z = False
    else:
        arr.append(arr.popleft())

        z = True

for i in answer:
    print(i, end=' ')
