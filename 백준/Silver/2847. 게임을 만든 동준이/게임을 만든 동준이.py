n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

cnt = 0

for i in range(n-1, 0, -1):
    if arr[i] <= arr[i-1]:
        while arr[i] <= arr[i-1]:
            cnt += 1
            arr[i-1] = arr[i-1] - 1
# for i in range(n-1, -1, -1):
#     if i == 0:
#         continue

#     elif i == n-1:
#         if arr[i] <= arr[i-1]:
#             while arr[i] <= arr[i-1]:
#                 arr[i-1] = arr[i-1] - 1
#                 cnt += 1
#     else:
#         pass

print(cnt)
