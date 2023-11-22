import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        i, j = 0, n-1
        flag = True
        while i < j:
            if lego[i] + lego[j] == x:
                print('yes %d %d' %(lego[i], lego[j]))
                flag = False
                break

            elif lego[i] + lego[j] < x:
                i += 1
            else:
                j -= 1
        if flag:
            print('danger')
    except:
        break