from collections import deque

a, b = map(int, input().split())

r = 1


def bfs(a, b):
    q = deque()
    q.append((a, 1))

    while q:
        a, count = q.popleft()

        if a == b:
            print(count)
            return

        if a * 2 <= b:
            q.append((a * 2, count + 1))
        if a * 10 + 1 <= b:
            q.append((a * 10 + 1, count + 1))
    print(-1)


bfs(a, b)
