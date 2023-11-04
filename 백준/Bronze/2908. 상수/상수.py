a, b = map(int, input().split())

a = str(a)
b = str(b)
a = [i for i in a]
b = [i for i in b]
a.reverse()
b.reverse()

a = (''.join(a))
b = ''.join(b)

a = int(a)
b = int(b)

answer = max(a, b)

print(answer)