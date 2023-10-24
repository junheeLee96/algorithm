import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))


fuel = 1010101010101010

dy = [0, -1, 1]


def dfs(x, y, p_y, num, ff):
    if x == n-1:
        return min(ff, num)

    for i in range(3):
        if dy[i] == p_y:
            continue
        else:
            nx = x + 1
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                num = dfs(nx, ny, dy[i], num, ff + arr[nx][ny])

    return num


for i in range(m):

    fuel = min(dfs(0, i, 100, fuel, arr[0][i]), fuel)

print(fuel)