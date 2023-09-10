n = int(input())
cnt,summ = 0,0
start, end = 0,0

while end<=n:
    if summ < n:
        end += 1
        summ += end
    elif summ > n:
        summ -= start
        start += 1
    else:
        cnt+=1
        end+=1
        summ+=end
print(cnt)