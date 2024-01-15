import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

arr = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
    arr[b].append([a, c])


def bfs(v):
    answer = 0

    longer = 0
    visit = [False] * (n+1)
    visit[v] = True
    q = deque()
    q.append((v, 0))

    while q:
        x, cnt = q.popleft()

        if answer < cnt:
            # global answer
            longer = x
            answer = cnt

        for i in arr[x]:
            if visit[i[0]] == False:
                visit[i[0]] = True
                q.append((i[0], i[1]+cnt))

    return longer, answer


ans, l = bfs(1)
# print(ans, l)

ans, l = bfs(ans)

print(l)

# print(longer, answer)


# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())

# arr = [[] for _ in range(n+1)]

# for _ in range(n-1):
#     a, b, c = map(int, input().split())
#     arr[a].append([b, c])
#     arr[b].append([a, c])


# answer = 0


# def bfs(v):
#     visit = [False] * (n+1)
#     q = deque()
#     q.append((v, 0))
#     visit[v] = True

#     while q:
#         global answer
#         x, cnt = q.popleft()

#         answer = max(cnt, answer)

#         for i in arr[x]:
#             if not visit[i[0]]:
#                 q.append((i[0], cnt+i[1]))
#                 visit[i[0]] = True


# for i in range(1, n+1):
#     bfs(i)

# print(answer)
