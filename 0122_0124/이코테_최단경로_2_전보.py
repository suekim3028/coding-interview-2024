import datetime
import sys
import heapq

input = sys.stdin.readline

def try1():
    # 시작: 2024-01-24 10:40:44.037573
    # 종료: 2024-01-24 11:00:15.462487

    INF = int(10e9)
    n,m,c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    time_arr = [INF] * (n+1)

    for _ in range(m):
        from_n,to_n,time = map(int, input().split())
        graph[from_n].append([to_n, time])

    print("graph:",graph)
    print("time_arr:",time_arr)

    def dij():
        q = []
        heapq.heappush(q, (0, c))
        time_arr[c] = 0

        while(q):
            min_time, from_n = heapq.heappop(q)
            print(from_n, min_time)
            if(time_arr[from_n]<min_time): continue
            for a in graph[from_n]:
                to_n, time = a
                print("to:",to_n,"/ time:", time)
                if(time_arr[to_n] > min_time + time):
                    time_arr[to_n] = min_time + time
                    heapq.heappush(q, (min_time+time, to_n))
        
    dij()

    total_city=0
    total_time=0

    print(graph)
    print(time_arr)
    
    for i in range(1,n+1):
        if(i == c or time_arr[i]==INF): continue
        total_city+=1
        total_time = max(total_time, time_arr[i])

    print(total_city, total_time)

print(datetime.datetime.now())
try1()