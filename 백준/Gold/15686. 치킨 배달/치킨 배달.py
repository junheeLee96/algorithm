import math
import sys
from itertools import combinations
input = sys.stdin.readline
INF = math.inf

maps = []

n, m = map(int, input().split())

chick, home = [], []

for i in range(n):
    l = list(map(int, input().split()))

    for j in range(n):
        if l[j] == 1:
            home.append([i, j])
        elif l[j] == 2:
            chick.append([i, j])

    maps.append(l)

answer = INF
for chick_list in combinations(chick, m):
    # print(chick_list)
    city = 0

    for i in home:
        dist = INF
        home_r1, home_c1 = i[0], i[1]

        for chick_position in chick_list:
            chick_r2, chick_c2 = chick_position[0], chick_position[1]

            r = abs(home_r1 - chick_r2) + abs(home_c1 - chick_c2)

            dist = min(dist, r)

        city += dist

    answer = min(city, answer)

print(answer)
