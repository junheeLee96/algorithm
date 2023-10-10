# from collections import deque

# n, m = map(int, input().split())

# ladder = []
# snake = []

# for _ in range(n):
#     a, b = map(int, input().split())
#     ladder.append([100-a, 100-b])

# for _ in range(m):
#     a, b = map(int, input().split())
#     snake.append([100-a, 100-b])

# arr = [[False for _ in range(10)] for _ in range(10)]

# result = 9999999999999999999


# def bfs():
#     q = deque()
#     q.append((9, 9, 0))
#     arr[9][9] = True

#     while q:
#         x, y, cnt = q.popleft()

#         if x == 0 and y == 0:
#             # 골인지점
#             print(cnt)
#             return

#         is_ladder = False

#         for l in range(len(ladder)):
#             if ladder[l][0] == int(str(x) + str(y)):

#                 # 사다리를 만낫다면
#                 new_position = str(ladder[l][1])
#                 if len(new_position) == 1:
#                     new_position = '0' + new_position
#                 q.append((new_position[0], new_position[1], cnt))
#                 arr[int(new_position[0])][int(new_position[1])] = True
#                 is_ladder = True
#         if is_ladder == True:
#             continue

#         is_snake = False

#         for s in range(len(snake)):
#             # 뱀을 만나면
#             if snake[s][0] == int(str(x) + str(y)):
#                 is_snake = True

#         if is_snake == True:
#             continue

#         for i in range(1, 7):
#             now = int(str(x) + str(y))
#             now -= i

#             if now < 0:
#                 # 맵을 벗어나면
#                 continue

#             now = str(now)

#             if len(now) == 1:
#                 now = '0' + now

#             # for s in range(len(snake)):
#             #     # 뱀을 만나면
#             #     if snake[s][0] == int(str(x) + str(y)):
#             #         is_snake = True

#             # if is_snake == True:
#             #     continue

#             nx = int(now[0])
#             ny = int(now[1])

#             if arr[nx][ny] == True:
#                 continue

#             arr[nx][ny] = True
#             q.append((nx, ny, cnt+1))


# bfs()


from collections import deque


n, m = map(int, input().split())

ladder = []
snake = []

for _ in range(n):
    a, b = map(int, input().split())
    ladder.append([a, b])

for _ in range(m):
    a, b = map(int, input().split())
    snake.append([a, b])

arr = [0] * 101
visit = [False] * 101


q = deque()

q.append((1))

while q:
    x = q.popleft()

    if x == 100:
        # 탈출 조건
        print(arr[x])
        break

    for i in range(1, 7):
        # 주사위 굴리기
        nx = x + i

        if nx > 100:
            continue
        if visit[nx] == True:
            continue

        for l in range(len(ladder)):
            if ladder[l][0] == nx:
                nx = ladder[l][1]

        is_snake = False

        for s in range(len(snake)):
            if snake[s][0] == nx:
                nx = snake[s][1]

        if is_snake:
            continue
        if visit[nx] == True:
            continue
        visit[nx] = True

        arr[nx] = arr[x] + 1

        q.append((nx))
