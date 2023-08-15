a,b = map(str,input().split())

mm = 99

for i in range(len(b) + 1 - len(a)):
  m = 0
  for j in range(len(a)):
    if a[j] != b[i+j] :
      # print(i,j)
      # print(a[j],b[i+j])
      # print('-----')
      m += 1
  if mm > m:
    mm =m

print(mm)