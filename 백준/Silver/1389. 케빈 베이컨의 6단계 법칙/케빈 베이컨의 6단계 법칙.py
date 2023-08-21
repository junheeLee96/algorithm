from collections import deque

n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]

answer = [99998999999999999999999999999999999999999999, 0]

# for i in range()

for i in range(m):
    a, b = map(int, input().split())

    arr[a].append(b)
    arr[b].append(a)


def bfs(idx):
    q = deque()

    q.append((idx, 0))

    sum_distance = 0
    visit = [False for _ in range(n + 1)]

    while q:
        idx, distance = q.popleft()
        visit[idx] = True
        sum_distance += distance

        for i in arr[idx]:
            if visit[i] == False:
                # print(arr[idx])

                q.append((i, distance + 1))
                visit[i] = True

    return (sum_distance)


for i in range(1, n + 1):
    distance = bfs(i)
    if answer[0] > distance:
        answer = [distance, i]
    # answer.append(distance)
print(answer[1])
# print(answer.index(min(answer)))
