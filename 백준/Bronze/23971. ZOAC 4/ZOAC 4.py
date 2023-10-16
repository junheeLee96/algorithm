H,W,N,M = list(map(int,input().split(' ')))
#math.ceil()함수는 숫자의 올림을 계산해 줍니다
import math
a = math.ceil(H/(N+1)) # 세로에 몇 명이 앉는지를 계산합니다
b = math.ceil(W/(M+1)) # 가로에 몇 명이 앉는지를 계산합니다
answer = a*b #가로와 세로의 값을 곱합니다
print(answer)