n = int(input())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

dic = {}

a.sort()

b.sort(reverse=True)
answer= 0
for i in range(len(a)):
  answer += a[i] * b[i]
print(answer)