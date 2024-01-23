import datetime
import sys
import heapq

input = sys.stdin.readline

def try1():
    # 2024-01-23 14:52:02.248198
    # 2024-01-23 15:07:08.496005
    INF = int(10e9)
    n,m = map(int, input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for _ in range(m): 
        from_n, to_n = map(int, input().split())
        graph[from_n][to_n] = 1
        graph[to_n][from_n] = 1

    for i in range(1,n+1):
        graph[i][i] = 0

    x,k = map(int, input().split()) ## 문제 잘봐!!!!!

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                if(graph[j][k]>graph[j][i]+graph[i][k]):
                    graph[j][k] = graph[j][i]+graph[i][k]
    print(graph[1][k]+graph[k][x])

print(datetime.datetime.now())
try1()