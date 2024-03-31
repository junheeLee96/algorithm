import sys
input = sys.stdin.readline

n = int(input())

c = []

for _ in range(n):
    # a, b = map(int, input().split())
    # l = list(map(int,))
    # c.append([a, b])
    a, k = map(int, input().split())
    c.append([a, k])

c.sort(key=lambda x: x[0])

ans = 0

for i in range(n):
    if ans >= c[i][0]:
        ans += c[i][1]
    else:
        ans = ans + (c[i][0] - ans + c[i][1])
    # print('i = ', i, ans)


print(ans)
