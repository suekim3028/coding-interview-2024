import sys
input = sys.stdin.readline
import heapq


# 방문한 노드들에 대한 정보 가짐
# 각 노드들에 대한 최단 거리 가짐 -> INF 로 초기화
# 방문 안한 노드들 중 최단 거리인 애 꺼내서 방문
# 해당 노드


def try1():
    INF = int(10e9)
    n,m = map(int,input().split())
    start = int(input())

    graph = [[] for _ in range(n+1)]
    visited = [False]  * (n+1)
    dist = [INF] * (n+1)

    for i in range(m):
        from_n, to_n, d= map(int, input().split())
        graph[from_n].append((to_n,d))

    
    dist[start] = 0
    visited[start] = True

    for to_n, d in graph[start]:
        dist[to_n] = d

    def getSmallest():
        smallest= INF
        index = 0
        for i in range(1,n+1):
            if(visited[i]==False):
                if(dist[i]<smallest):
                    smallest = dist[i]
                    index = i
        return index
    
    while(False in visited):
        smallest = getSmallest()
        visited[smallest] = True
    
        for to_n, d in graph[smallest]:
            if(dist[to_n] > dist[smallest] + d):
                dist[to_n] = dist[smallest] + d

    print(dist)


input = sys.stdin.readline
def try2():
    INF = int(10e9)
    n,m = map(int, input().split())
    start = int(input())
    
    dist = [INF] * (n+1)

    graph = [[] for _ in range(n+1)] 

    for _ in range(m):
        from_n, to_n, d = map(int, input().split())
        graph[from_n].append((to_n, d))


    dist[start] = 0

    q = []
    heapq.heappush(q, (start, 0))

    while(q):
        # 가운데 애를 꺼내는 중 -> 우선 현재로서는 dist -> to_n 이 젤 짧아야함
        pass_n, d = heapq.heappop(q)
        if(dist[pass_n]<d):
            continue
        
        for to_n, to_dist in graph[pass_n]:
            if(dist[to_n]> d+to_dist ):
                dist[to_n] = d+to_dist
                heapq.heappush(q,(to_n, d+to_dist))
    print(dist)


try2()









