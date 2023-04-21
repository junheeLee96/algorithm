a = int(input())


#25 10 5 1

arr = [0,0,0,0]

for i in range(a):
    arr=[0,0,0,0]
    n = int(input())
    
    while n >0 :
        if n >= 25:
            arr[0] = n // 25;
            n = n % 25
        elif n >= 10:
            arr[1] = n // 10
            n = n % 10
        elif n >= 5:
            arr[2] = n // 5
            n = n  % 5
        else:
            arr[3] = n // 1
            n = n % 1
    for j in arr:
        print(j, end=' ')