def fn():
    INF = int(10e9)
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for i in range(n+1)] # *(n+1) 로 하면 depth 하나 이상으로 올라갔을때 pointer 됨 ㄷㄷ
    
    for i in range(1,n+1):
        graph[i][i] = 0
    
    for _ in range(m):
        from_n, to_n, dist = map(int, input().split())
        graph[from_n][to_n] = dist
    
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if(graph[j][k] > graph[j][i] + graph[i][k]):
                    graph[j][k] = graph[j][i] + graph[i][k]
    
    for i in range(1,n+1):
        for j in range(1, n+1):
            item = graph[i][j]
            print("INF" if item == INF else item, end = " ")
        print() 

fn()

