
from sys import stdin
input = stdin.readline

# 입력값 받기
n, m = map(int, input().split())
relations = [[] for _ in range(n)]
# 방문 표시
visited = [False] * 2001
# 정답 변수 생성
ans = False
# 친구 관계 입력받기
for i in range(m):
    a, b = map(int, input().split())
    # 친구 관계 등록
    relations[a].append(b)
    relations[b].append(a)

# dfs 이용
def dfs(idx, depth):
    global ans
    visited[idx] = True
    # 친구 관계가 4번 이상 연결되어 있다면
    if depth == 4:
        # 정답 표시 후 리턴
        ans = True
        return
    # 친구 관계가 존재하는지 확인
    for i in relations[idx]:
        # 아직 방문하지 않았다면
        if not visited[i]:
            # 방문 표시
            visited[i] = True
            # 재귀적으로 수행
            dfs(i, depth + 1)
            # 방문 표시 해제
            visited[i] = False

# 0번부터 N-1번까지 확인하며
for i in range(n):
    # 친구 관계 탐색
    dfs(i, 0)
    # 현재 방문 표시 해제
    visited[i] = False
    # 친구 관계가 존재한다면
    if ans:
        # 탈출
        break
# 정답이 있다면 1 출력
if ans:
    print(1)
# 정답이 없다면 0 출력
else:
    print(0)