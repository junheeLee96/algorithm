from itertools import combinations

arr = []

for _ in range(9):
    arr.append(int(input()))

for talls in combinations(arr, 7):
    if sum(talls) == 100:
        answer = sorted(talls, key=lambda x: x)
        for i in answer:
            print(i)
        break
