import sys
input = sys.stdin.readline
import heapq

def try1():
    INF = int(10e9)
    n,m = map(int , input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    dist_arr = [INF]*(n+1)

    for _i in range(m):
        from_node, to_node, dist = map(int, input().split()) 
        graph[from_node].append([to_node, dist])
    
    print(graph)
    def dijkstra(start):
        q = []
        heapq.heappush(q, (start,0))
        dist_arr[start] = 0

        while q:
            from_node, now_dist = heapq.heappop(q)
            print("from_node: ", from_node, ", now_dist: ", now_dist )
            if(dist_arr[from_node]<now_dist): 
                continue
            for i in graph[from_node]:
                to_node = i[0]
                _dist = i[1]
                if(dist_arr[to_node]>now_dist + _dist):
                    dist_arr[to_node]=now_dist+_dist
                    heapq.heappush(q, (to_node, now_dist+_dist))
    
    dijkstra(start)
    for i in dist_arr:
        print("INFINITY" if i == INF else i)
            

def test2():
    
    INF = int(10e9)
    n, m = map(int, input().split())
    start = int(input())

    print("===========")
    
    graph = [[] for _i in range(m+1)]
    dist_arr = [INF] * (m+1)
    for _i_ in range(m):
        from_node, to_node, dist = map(int, input().split())
        graph[from_node].append([to_node, dist])
    
    def dijkstra(start):
        q = []
        dist_arr[start] = 0
        heapq.heappush(q, [start, 0])
        
        while q: 
            destination, min_dist = heapq.heappop(q)
            if(dist_arr[destination]<min_dist):
                continue
            
            for [to_node, dist] in graph[destination]:
                new_dist = dist + min_dist
                if(dist_arr[to_node]>new_dist):
                    dist_arr[to_node] = new_dist
                    heapq.heappush(q, [to_node, new_dist])
        for i in dist_arr:
            print("INFINITY" if i==INF else i)
            
    dijkstra(start)
    
    
test2()


