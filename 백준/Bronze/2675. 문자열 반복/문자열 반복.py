t = int(input())

for _ in range(t):
    n, s = map(str, input().split())

    n = int(n)
    new = ''
    for i in range(len(s)):
        for _ in range(n):
            new += s[i]

    print(new)
