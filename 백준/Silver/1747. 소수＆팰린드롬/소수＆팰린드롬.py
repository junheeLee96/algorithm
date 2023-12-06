import math

def isPrime(x): # 소수인지 판별해주는 함수
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

N = int(input())
result = 0

for i in range(N, 1000001): # 입력값 N 부터 최대값 까지 순환
    if i == 1: # 1은 소수가 아니기 때문에 예외처리
        continue
    if str(i) == str(i)[::-1]: # 팰림드롬 수 일 경우
        if isPrime(i) == True: # 소수 판별 함수 적용
            result = i
            break

if result == 0: # 입력값이 만약 최대 값 100만일 경우
    result = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용

print(result)