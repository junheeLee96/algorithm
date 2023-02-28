a = int(input())

arr = []

for i in range(a):
  arr.append(list(map(int,input().split())))


for i in range(1,len(arr)):
  for j in range(len(arr[i])):
    left = 0
    right = 0
    if j - 1 >= 0:
      left = arr[i-1][j-1] + arr[i][j]
    if len(arr[i -1]) > j:
      right = arr[i-1][j] + arr[i][j]
      

    arr[i][j] = max(left,right)

print(max(arr[-1]))