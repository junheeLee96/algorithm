import sys
input = sys.stdin.readline


def dfs(v, i):
    visit[v] = True
    w = data[v]
    if not visit[w]:
        dfs(w, i)
    elif visit[w] and w == i:
        result.append(w)


n = int(input())
data = [0] + [int(input()) for _ in range(n)]

result = []

for i in range(1, n+1):
    visit = [False]*(n+1)
    dfs(i, i)


print(len(result))
result.sort()
for i in result:
    print(i)
