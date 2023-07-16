from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)


visit = [False] * (n + 1)

cnt = 0

for i in range(1, len(arr)):
    if visit[i] == False:
        if not arr[i]:
            cnt += 1
            visit[i] = True
        else:
            q = deque()
            q.append(i)
            visit[i] = True
            while q:
                k = q.popleft()

                for a in arr[k]:
                    if visit[a] == False:
                        visit[a] = True
                        q.append(a)
            cnt += 1

print(cnt)
