from collections import deque


n = int(input())

arr = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    arr[a].append(b)
    arr[b].append(a)


def bfs(x):
    visit = [-1 for _ in range(n+1)]
    visit[x] = 0
    q = deque()
    q.append((x))

    while q:
        num = q.popleft()

        for i in arr[num]:
            if visit[i] == -1:
                visit[i] = visit[num] + 1
                q.append(i)

    return max(visit)


score = 50
lst = []

for i in range(1, n+1):
    tmp = bfs(i)
    if tmp < score:
        score = tmp
        lst = [i]
    elif tmp == score:
        lst.append(i)
print(score, len(lst))
print(*lst)
