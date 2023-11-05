n = int(input())

init = n
n = str(n)
if len(n) == 1:
    n = '0' + n

i = 1

p = n

n = int(n[0]) + int(n[1])
n = str(n)

if len(n) == 1:
    n = p[-1] + n
else:
    n = p[-1] + n[-1]

while True:
    if int(init) == int(n):
        break


# while True:
    i += 1
#     if init == int(n):
#         break

    prev = n

    n = int(n[0]) + int(n[1])

    n = str(n)

    if len(n) == 1:
        n = prev[-1] + n

    else:
        n = prev[-1] + n[-1]
    # print(n)


print(i)