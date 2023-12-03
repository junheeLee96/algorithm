s = input()  # 문자열 입력
a = s.count('a')  # 입력된 str에서의 a의 개수

answer = float('inf')


s = s + s[0:a-1]


for i in range(len(s) - (a-1)):

    answer = min(answer, s[i:i+a].count('b'))

print(answer)