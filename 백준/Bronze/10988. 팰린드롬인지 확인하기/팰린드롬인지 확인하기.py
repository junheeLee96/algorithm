s = input()

r = ''

for i in range(len(s)-1, -1, -1):
    r += s[i]

if r == s:
    print(1)
else:
    print(0)
