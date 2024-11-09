def solution(n, s, a, b, fares):
    answer = 0
    INF = 1000001
    graph = [ [INF ] * (n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for i in fares:
        one,two,p = i
        graph[one][two] = p
        graph[two][one] = p
        
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][j] == INF:
                    graph[i][j] =  graph[i][k] + graph[k][j]
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    answer = graph[s][a] + graph[s][b]
    for i in range(1,n+1):
        if graph[i][s] != INF and graph[i][a] != INF and graph[i][b] != INF:
            answer = min(answer, graph[i][a] + graph[i][b] + graph[i][s])
            
    return answer