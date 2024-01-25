n, m = map(int, input().split())

arr = [[] for _ in range(n)]

ans = False

visit = [False for _ in range(2001)]

for _ in range(m):
    a, b = map(int, input().split())

    arr[b].append(a)
    arr[a].append(b)


def dfs(idx, dep):
    visit[idx] = True
    if dep == 4:
        global ans
        ans = True

        return

    for i in arr[idx]:
        if visit[i] == False:
            visit[i] = True
            dfs(i, dep + 1)

            visit[i] = False


for i in range(n):
    dfs(i, 0)
    visit[i] = False
    if ans:
        break


if ans:
    print(1)
else:
    print(0)
