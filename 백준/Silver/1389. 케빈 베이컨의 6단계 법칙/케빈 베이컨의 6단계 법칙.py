from collections import deque

# 유저의 수와 관계의 개수를 입력 받음
users, relationships = map(int, input().split())

# 각 유저의 친구 관계를 저장하는 리스트
arr = [[] for _ in range(users + 1)]

# 친구 관계를 입력 받아 리스트에 저장
for _ in range(relationships):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 각 유저의 케빈 베이컨 수를 계산하는 함수
def kevin_bacon(user):
    q = deque()
    q.append((user, 0))
    visited = [False] * (users + 1)
    visited[user] = True
    total_distance = 0

    while q:
        curr_user, distance = q.popleft()
        total_distance += distance

        for friend in arr[curr_user]:
            if not visited[friend]:
                q.append((friend, distance + 1))
                visited[friend] = True

    return total_distance

min_kevin_bacon = float('inf')  # 최소 케빈 베이컨 수 초기화
min_user = -1  # 최소 케빈 베이컨 수를 가진 유저 번호 초기화

# 각 유저의 케빈 베이컨 수를 계산하고, 가장 작은 값을 가진 유저 찾기
for user in range(1, users + 1):
    user_kevin_bacon = kevin_bacon(user)
    
    if user_kevin_bacon < min_kevin_bacon:
        min_kevin_bacon = user_kevin_bacon
        min_user = user

print(min_user)