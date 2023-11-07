n = int(input())

s = input()

s = s.replace('LL', 'L')

new_s = '*'

for i in range(len(s)):
    new_s += s[i]
    new_s += '*'

s = new_s.replace('L', 'LL')

arr = []

for i in s:
    if i == '*':
        arr.append(False)
    else:
        arr.append(i)


cnt = 0

for i in range(len(arr)):
    if arr[i] == False or arr[i] == True:
        continue
    else:
        if arr[i - 1] == False:
            cnt += 1
            arr[i-1] = True
        elif arr[i+1] == False:
            arr[i+1] = True
            cnt += 1

print(cnt)
