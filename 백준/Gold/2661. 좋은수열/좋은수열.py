n = int(input())


def check(s):

    for i in range(0, len(s)//2 + 1):
        if s[-i:] == s[-(i*2):-i]:
            return False

    return True


def dfs(s):

    if len(s) == n:
        print(s)
        exit()

    for i in '123':
        if check(s+i):
            dfs(s+i)


dfs('1')
