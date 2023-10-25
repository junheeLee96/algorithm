n, x = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = x

max_sum = sum(arr[left:right])

left += 1
right += 1

prev_range = max_sum

cnt = 1

while right <= n:
    this_range = prev_range - arr[left-1]
    this_range += arr[right-1]

    if this_range > max_sum:
        cnt = 1
        max_sum = this_range
    elif this_range == max_sum:
        cnt += 1

    prev_range = this_range
    left += 1
    right += 1


if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(cnt)
