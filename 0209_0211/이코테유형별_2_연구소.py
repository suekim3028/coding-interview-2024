import sys
import itertools
import copy
import datetime
from collections import deque

input = sys.stdin.readline








def try1():
    # 2024-02-10 03:40:15.504195
    # 2024-02-10 04:41:25.720306

    n,m= map(int, input().split())
    _graph = []

    zeros = []
    twos = []

    for i in range(n):
        row = list(map(int, input().split()))
        _graph.append(row)
        for j in range(m):
            item = row[j]
            if(item==0):
                zeros.append((i,j))
            if(item==2):
                twos.append((i,j))
            
    res = 0

    for walls in itertools.combinations(zeros, 3):
        graph = [[_graph[i][j] for j in range(m)] for i in range(n)]

        for wall in walls:
            graph[wall[0]][wall[1]] = 1
            
        _res = 0
        
        q = deque(twos)
                    
        while(q):
            x,y = q.popleft()
            for dx, dy in [(1,0), (0,1),(-1,0),(0,-1)]:
                next_x = min(max(x+dx, 0),n-1)
                next_y = min(max(y+dy,0), m-1)
                
                if(next_x == x and next_y == y):
                    continue
                    
                if(graph[next_x][next_y]==0):
                    graph[next_x][next_y]=2
                    q.append((next_x, next_y))
                    
        _res = sum([i.count(0) for i in graph])
        res = max(_res, res)
        
    print(res)

    return

print(datetime.datetime.now())
try1()
