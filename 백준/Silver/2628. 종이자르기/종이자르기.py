import sys
input = sys.stdin.readline

n, m = map(int, input().split())

k = int(input())

width = [0, n]
height = [0, m]

for _ in range(k):
    a, b = map(int, input().split())

    if a == 0:
        height.append(b)
    else:
        width.append(b)

width.sort()
height.sort()


answer = 0

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        row = width[i+1] - width[i]
        col = height[j+1] - height[j]
        answer = max(answer, (row*col))

print(answer)
