
n = int(input())

arr = []

for i in range(n):
    arr.append(input())

m_width, m_height = 0, 0


for i in range(n):
    width, height = 0, 0
    for j in range(n):
        if arr[i][j] == '.':
            width += 1
        else:
            width = 0

        if width == 2:
            m_width += 1

        if arr[j][i] == '.':
            height += 1

        else:
            height = 0

        if height == 2:
            m_height += 1

print(m_width, m_height)