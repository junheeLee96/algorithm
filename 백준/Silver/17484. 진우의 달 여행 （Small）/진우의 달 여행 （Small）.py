import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


fuel = 1010101010101010

dy = [0, -1, 1]


def dfs(x, y, p_y, fff, now_position_fuel):
    if x == n-1:
        return min(now_position_fuel, fff)

    for i in range(3):
        if dy[i] == p_y:
            continue
        else:
            nx = x + 1
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                fff = dfs(nx, ny, dy[i], fff, now_position_fuel + arr[nx][ny])

    return fff


for i in range(m):

    fuel = min(dfs(0, i, 100, fuel, arr[0][i]), fuel)

print(fuel)


# 6 4
# 5 8 5 1
# 3 5 8 4
# 9 77 65 5
# 2 1 5 2
# 5 98 1 5
# 4 95 67 58
