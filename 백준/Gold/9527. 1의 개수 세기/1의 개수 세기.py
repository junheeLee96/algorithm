def count(num):  
    cnt = 0  
    bin_num = bin(num)[2:]  
    length = len(bin_num)  
    for i in range(length):  
        if bin_num[i] == '1':  
            # num보다 크지 않으면서 가장 큰 2의 거듭제곱 수  
            val = length-i-1  
            cnt += one_sum[val]  
            # 가장 앞자리 1 개수를 추가로 더해주기  
            cnt += (num - 2**val + 1)  
            num = num - 2 ** val  
    return cnt  

x, y = map(int, input().split())  
one_sum = [0 for _ in range(60)]  

for i in range(1, 60):  
    one_sum[i] = 2**(i-1) + 2 * one_sum[i-1]  

print(count(y) - count(x-1))

# https://cheon2308.tistory.com/entry/%EB%B0%B1%EC%A4%80-9527%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC-1%EC%9D%98-%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0
# 위 링크 참조