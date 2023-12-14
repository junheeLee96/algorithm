
s = input()

dic = {
    'c=': 0,
    'c-': 0,
    'dz=': 0,
    'd-': 0,
    'lj': 0,
    'nj': 0,
    's=': 0,
    'z=': 0
}

cnt = 0

# for key in dic.keys():
#     if key in s:
#         for i in range(0, len(s), len(key)):
#             if s[i:i+len(key)] == key:

#                 print(s[i:i+len(key)])


for key in dic.keys():
    if key in s:

        length = len(key)
        while True:
            idx = s.index(key)
            s = s[:idx] + '0'+s[idx+length:]
            cnt += 1
            # print(s)
            # print(key, s, cnt, idx, length)
            if key not in s:
                break

for i in s:
    if i != '0':
        cnt += 1

print(cnt)
