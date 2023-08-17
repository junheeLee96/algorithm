n = int(input())

arr = []

for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

max_price = 0


def dfs(idx, select, sum_price):
    if idx > len(arr)-1:
        return sum_price

    if select:
        if idx + arr[idx][0] - 1 > len(arr)-1:
            return sum_price

        sum_price += arr[idx][1]
        new_idx = idx + arr[idx][0]
        return max(dfs(new_idx, True, sum_price), dfs(new_idx, False, sum_price))

    else:
        if idx + 1 > len(arr)-1:
            return sum_price
        return max(dfs(idx+1, True, sum_price), dfs(idx+1, False, sum_price))


# def dfs(idx, select, sum_price):


print(max(dfs(0, False, 0),
      dfs(0, True, 0)))
