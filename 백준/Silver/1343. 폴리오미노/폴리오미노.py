s = input()

s = s.replace('XXXX', '4')

# print(s)

s = s.replace('XX', '2')

# print(s)
is_ = False
for i in s:
    if i == 'X':
        print(-1)
        is_ = True
        break
if is_ == False:
    s = s.replace('2', 'BB')
    s = s.replace('4', 'AAAA')
    print(s)