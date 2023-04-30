n = int(input())

arr = []
weights = []

for i in range(n):
    arr.append(int(input()))
    weights.append(0)

arr.sort(reverse=True)


for i in range(len(arr)):
    weights.append((i+1) * arr[i])

print(max(weights))