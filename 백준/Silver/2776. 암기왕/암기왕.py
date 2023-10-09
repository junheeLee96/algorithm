from bisect import bisect_left

t = int(input())


def find():
    n = int(input())

    arr = list(map(int, input().split()))
    m = int(input())

    arr2 = list(map(int, input().split()))

    arr.sort()

    for i in range(len(arr2)):
        target = arr2[i]

        start = 0
        end = n-1

        while start <= end:
            mid = (start + end) // 2

            if target == arr[mid]:
                print(1)
                break

            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

        if start > end:
            print(0)


for _ in range(t):
    find()
