n = int(input())

head = []

heart = []

left_arm = 0

right_arm = 0

mid = 0

left_leg = 0
right_leg = 0

for i in range(n):
    string = input()

    for j in range(len(string)):
        if string[j] == '*':
            if head == []:
                # 헤드를 발견하지 못햇다면
                # 맨처음 *은 무조건 헤드임
                head = [i, j]
            else:
                if heart == []:
                    # 하트가 비엇다면 왼쪽팔이나 하트라는 뜻
                    if head[1] == j:
                        # 헤드 바로 아래, 즉 하트라면 하트 위치 저장
                        heart = [i, j]
                    else:
                        # 하트가 비어잇고 머리 바로 아래가 아니라면, 즉 왼쪽 팔이라는 뜻
                        left_arm += 1
                else:
                    # 하트가 비어잇지 않다면
                    #  여기 부터는 오른쪽 팔, 허리, 다리가 될수가 잇다
                    if i == heart[0]:
                        # 가로로 하트와 일직선상이라면, 즉 오른쪽 팔이라면
                        right_arm += 1

                    else:
                        # 하트가 차있고, 하트와 가로로 일직선상이 아니라면
                        if j == heart[1]:
                            # 만약 하트와 세로로 일직선상이라면
                            mid += 1
                        else:
                            # 여기서부턴 왼다리 또는 오른다리 둘중 하나이다
                            if heart[1] > j:
                                # 하트와 세로로 일직선상에서 왼쪽에서 있다면 왼쪽다리이다
                                left_leg += 1
                            else:
                                right_leg += 1

print(heart[0]+1, heart[1]+1)
print(f'{left_arm} {right_arm} {mid} {left_leg} {right_leg}')
