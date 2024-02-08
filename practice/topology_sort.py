# 위상 정렬
# 방향대로 그래프 노드 정렬

# 큐 돌면서 노드로 들어오는 엣지 없으면 넣고 해당 노드에서 나가는 엣지 다 없앰
# 큐 빌때까지 반복


from collections import deque

v, e = map(int, input().split())
indgree = [0] * (v+1)
edges = [[] for _ in range(v+1)] # from -> to

for _ in range(e):
    from_n, to_n = map(int, input().split())
    edges[from_n].append(to_n)    
    indgree[to_n]+=1

q = deque()
res = []

for i in range(1, v+1):
    if(indgree[i] == 0):
        q.append(i)

while(q):
    node = q.popleft()
    res.append(node)
    for to_n in edges[node]:
        indgree[to_n] -=1
        if(indgree[to_n] == 0):
            q.append(to_n)

print(res)
        









