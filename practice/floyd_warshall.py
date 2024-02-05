import sys

input = sys.stdin.readline

def try1():
    INF = int(10e9)
    n,m = map(int, input().split())
    dist = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    for _ in range(m):
        from_n, to_n, d = map(int, input().split())
        dist[from_n][to_n] = d

    for i in range(1,n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if(dist[i][k] > dist[i][j] + dist[j][k]):
                    dist[i][k] = dist[i][j] + dist[j][k]
    print(dist)     

try1()