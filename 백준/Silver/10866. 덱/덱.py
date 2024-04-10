from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

arr = deque()
# print('-----------')
for _ in range(n):

    s = input().split()
    # print(s)
    # continue
    if s[0] == 'push_front':
        arr.appendleft(s[1])
    elif s[0] == 'push_back':
        arr.append(s[1])

    elif s[0] == 'pop_front':
        if not arr:
            print(-1)
        else:
            print(arr.popleft())
            # arr = arr[1:]

    elif s[0] == 'pop_back':
        if not arr:
            print(-1)
        else:
            print(arr.pop())

    elif s[0] == 'size':
        print(len(arr))

    elif s[0] == 'empty':
        if not arr:
            print(1)
        else:
            print(0)

    elif s[0] == 'front':
        if not arr:
            print(-1)
        else:
            print(arr[0])

    elif s[0] == 'back':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
