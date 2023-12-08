from itertools import permutations

n, m = map(int, input().split())

arr = [i+1 for i in range(n)]

for li in permutations(arr, m):
    for num in li:
        print(num, end=' ')
    print()
