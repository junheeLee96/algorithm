dic = {}

# 'a'부터 'z'까지의 알파벳을 순회하며 딕셔너리에 키를 추가하고 값을 0으로 초기화합니다.
for char in 'abcdefghijklmnopqrstuvwxyz':
    dic[char] = 0

st = input()

st = st.lower()

for s in st:
    dic[s] += 1


sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

first_key, first_value = list(sorted_dict.items())[0]

# 두 번째 키와 밸류 얻기
second_key, second_value = list(sorted_dict.items())[1]

if first_value == second_value:
    print('?')
else:
    print(first_key.upper())
