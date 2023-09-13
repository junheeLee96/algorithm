

from collections import deque

n, k = map(int, input().split())

visit = [-1] * 100001
visit[n] = 0
q = deque()


q.append(n)

while q:
    idx = q.popleft()

    if idx == k:
        print(visit[k])
        break

    if 0 <= idx - 1 < 100001 and visit[idx-1] == -1:
        visit[idx-1] = visit[idx] + 1
        q.append(idx - 1)

    if 0 < idx * 2 < 100001 and visit[idx*2] == -1:
        visit[idx*2] = visit[idx]
        q.appendleft(idx*2)

    if 0 <= idx + 1 < 100001 and visit[idx+1] == -1:
        visit[idx+1] = visit[idx] + 1
        q.append(idx+1)
