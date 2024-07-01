a = int(input())

arr = list(map(int,input().split()))

arr.sort()

sums = 0

for i in range(len(arr)):
  sums = sums + arr[i]
  arr[i] = sums

print(sum(arr))