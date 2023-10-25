import sys
input = sys.stdin.readline
dic = {}


n, m = map(int, input().split())

for i in range(n):
    s = input().rstrip()

    if len(s) >= m:
        if s not in dic:
            dic[s] = 1

        else:
            dic[s] += 1


arr = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for i in arr:
    print(i[0])