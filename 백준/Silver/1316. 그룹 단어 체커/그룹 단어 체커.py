n = int(input())


cnt = 0

for _ in range(n):
    s = input()
    stack = []
    condition = True
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if i in stack:
                if stack[-1] == i:
                    stack.append(i)
                    continue
                else:
                    condition = False
                    break
            else:
                stack.append(i)

    if condition:
        cnt += 1

print(cnt)
