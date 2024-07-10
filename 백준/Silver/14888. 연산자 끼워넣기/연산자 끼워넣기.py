
import sys
import math
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

div = list(map(int, input().split()))


mx = -math.inf
mn = math.inf


def dfs(num, idx, plus, minus, multi, divide):
    if idx == n:
        global mx
        global mn
        mx = max(mx, num)
        mn = min(mn, num)
        return

    if plus > 0:
        dfs(num + arr[idx], idx + 1, plus - 1, minus, multi, divide)

    if minus > 0:
        dfs(num - arr[idx], idx + 1, plus, minus - 1, multi, divide)

    if multi > 0:
        dfs(num * arr[idx], idx + 1, plus, minus, multi - 1, divide)

    if divide > 0:
        if num < 0:
            dfs(-(-num // arr[idx]), idx + 1, plus, minus, multi, divide - 1)
        else:
            dfs(num // arr[idx], idx + 1, plus, minus, multi, divide - 1)


dfs(arr[0], 1, div[0], div[1], div[2], div[3])


print(mx, mn)


# for divs in permutations(div_arr, len(div_arr)):
# sm = 0
# num = arr[0]
# for i in range(1, n):
#     num = math.floor(int(eval(str(num) + divs[i-1] + str(arr[i]))))

# mx = max(mx, num)
# mn = min(mn, num)
