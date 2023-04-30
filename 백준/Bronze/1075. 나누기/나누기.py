
n = str(input())

f = int(input())



n = n[:-2]
# n = n[:-2] + '00'


for i in range(0,99):
    if i < 10:
        i = '0' + str(i)
    else:
        i = str(i)
        
    new_number = str(n) + i

    if int(new_number) % f == 0:
        print(i)
        break
# for i in range()