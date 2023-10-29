import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}
cnt = 0
for _ in range(n):
    s = input().strip()
    cnt += 1
    dic[s] = 1


for _ in range(m):
    st = input().strip()
    st = st.split(',')

    for j in st:
        if j in dic:
            cnt -= 1
            del dic[j]
    print(cnt)
