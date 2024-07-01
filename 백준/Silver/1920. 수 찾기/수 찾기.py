import sys

input = sys.stdin.readline

n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

arr1.sort()


def find(num):
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        # print(start, end, mid)

        if arr1[mid] == num:
            return 1

        if arr1[mid] > num:
            end = mid - 1
        elif arr1[mid] < num:
            start = mid + 1
    return 0


for i in arr2:
    print(find(i))
