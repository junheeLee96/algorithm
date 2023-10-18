dic = {}

user_input = input()

n, m = user_input.split()
n = int(n)

for _ in range(n):

    s = input()

    if s not in dic:
        dic[s] = 1


cnt = 0
if m == 'Y':
    cnt = 1
elif m == 'F':
    cnt = 2

else:
    cnt = 3

arr = list(dic.keys())

print(len(arr) // cnt)
