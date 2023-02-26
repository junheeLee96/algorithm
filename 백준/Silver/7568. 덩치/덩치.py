a = int(input())

arr = []

for _ in range(a):
  b = list(map(int,input().split()))
  arr.append(b)

answer = [1 for _ in range(a)]


for i in range(len(arr)):
  for j in range(len(arr)):
    if i == j:
      continue
    if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
     answer[i] += 1

for i in answer:
  print(i, end=" ")
    