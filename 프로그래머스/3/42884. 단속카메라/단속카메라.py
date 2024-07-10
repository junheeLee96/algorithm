def solution(routes):
    routes.sort(key=lambda x: (-x[1], -x[0]))
    routes = [routes[i] for i in range(len(routes)-1, -1, -1)]
    answer = 1
    last = routes[0][1]

    for i in range(1, len(routes)):
        if routes[i][0] <= last <= routes[i][1]:
            continue
        else:
            answer += 1
            last = routes[i][1]

    return answer