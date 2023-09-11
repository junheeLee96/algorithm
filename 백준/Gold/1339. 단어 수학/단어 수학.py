N = int(input())  # 단어의 개수 N 입력

words = []  # 단어를 저장할 리스트
for _ in range(N):
    words.append(input())

alpha_values = [0] * 26  # 알파벳에 대한 가중치를 저장할 리스트

# 각 알파벳의 가중치 계산
for word in words:
    word_len = len(word)
    for i in range(word_len):
        alpha_values[ord(word[i]) - ord('A')] += 10 ** (word_len - i - 1)
# 가중치가 큰 순서대로 정렬
alpha_values.sort(reverse=True)

# 가중치가 높은 알파벳부터 9부터 0까지 숫자를 할당
result = 0
for i in range(26):
    result += alpha_values[i] * (9 - i)
print(result)