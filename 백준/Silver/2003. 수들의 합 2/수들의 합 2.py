n,m = map(int,input().split())

arr = list(map(int,input().split()))

end = 1
answer = 0 
start = 0

while start <= end and end <= n:
  su =sum(arr[start:end])
   
  if su > m:
    start += 1
  elif su < m:
      end += 1
  elif su == m:
    answer += 1
    end += 1

print(answer)