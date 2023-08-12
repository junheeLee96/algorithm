from collections import deque

n, k = map(int, input().split())

q = deque([i for i in range(1, n+1)])

idx = 1

answer = []

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())


# 리스트의 요소들을 문자열로 변환
string_list = [str(item) for item in answer]

# 리스트의 문자열 요소들을 ', '로 조인하여 하나의 문자열로 만듦
result = "<" + ", ".join(string_list) + ">"

print(result)  # 출력: "<3, 6, 2, 7, 5, 1, 4>"
