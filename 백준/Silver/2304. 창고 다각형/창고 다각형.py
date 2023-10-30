n = int(input())

arr = [0 for _ in range(1001)]

mh = 0

height_idx = 0

for _ in range(n):
    idx, h = map(int, input().split())

    arr[idx] = h

    if mh < h:
        height_idx = idx
        mh = h
prev_h = 0
left_value = 0
for i in range(height_idx+1):
    if arr[i] == 0:
        left_value += prev_h
    else:
        if prev_h < arr[i]:
            prev_h = arr[i]
            left_value += arr[i]
        else:
            left_value += prev_h
    # print(
    #     f'i = {i}, arr[i] = {arr[i]}, prev_h = {prev_h}, left_value = {left_value}')
# print(left_value)


right_value = 0
prev_h = 0

for i in range(len(arr)-1, height_idx, -1):
    prev_h = max(arr[i], prev_h)
    right_value += prev_h
print(right_value + left_value)