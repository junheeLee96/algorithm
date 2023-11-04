n = int(input())


def dfs(n):
    if n == 0:
        return 1
    return n * dfs(n-1)


print(dfs(n))
