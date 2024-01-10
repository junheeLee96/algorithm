n, m = map(int, input().split())

arr = list(map(int, input().split()))

dp = [0]
for i in arr:
    if not dp:
        dp.append(i)
    else:
        dp.append(dp[-1]+i)

answer = 0

for i in range(1, len(dp)-m+1):
    # print(i, i+m-1)

    num = dp[i+m-1] - dp[i-1]

    answer = max(answer, num)

print(answer)
