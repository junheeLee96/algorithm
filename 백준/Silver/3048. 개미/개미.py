n1, n2 = map(int, input().split())
ant1 = list(input())
ant2 = list(input())
path = ant1[::-1] + ant2
t = int(input())
for _ in range(t):
    for i in range(len(path)-1):
        # 두 개미 그룹이 만났다면 자리를 바꾼다.
        if path[i] in ant1 and path[i+1] in ant2:
            path[i], path[i+1] = path[i+1], path[i]
            # 위치를 바꾼 개미가 선두 개미면 반복을 멈춘다. 
            if path[i+1] == ant1[0]:
                break
print(''.join(path))