import datetime
import sys
input = sys.stdin.readline



def try1():
    # 2024-02-10 02:31:11.925141
    # 
    v = int(input())
    e = int(input())
    INF = int(10e9)

    dist = [[INF]*(v+1) for _ in range(v+1)] 

    for i in range(1,v+1):
        dist[i][i] = 0

        
    for _ in range(e):
        a, b, cost = map(int, input().split())
        dist[a][b] = min(dist[a][b], cost)

    for i in dist:
        print(i)
    
    print("=======")
        
    for k in range(1, v+1):
        for i in range(1, v+1):
            for j in range(1, v+1):
                if(dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]

    for i in dist:
        print(i)

    print("=======")
    
    for i in range(1,v+1):
        for j in range(1,v+1):
            print(0 if dist[i][j]==INF else dist[i][j], end= " ")
        print("")
    return
print(datetime.datetime.now())
try1()