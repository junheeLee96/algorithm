s = input()

for i in range(ord('a'), ord('z')+1):
    idx = s.find(chr(i))

    print(idx)
