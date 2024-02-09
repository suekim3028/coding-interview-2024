# 크루스칼 알고리즘
# minimum spanning tree 를 찾는데 사용
# 그리디 알고리즘의 일종

# 1. 간선 비용 오름차순
# 2. 앞에서부터 보면서 사이클 없는 경우 포함시키고 두 노드 union



v,e = map(int, input().split())
parent = [0] * (v+1)

edges = []
res = 0


def find_parent(parent, x):
    if(parent[x]!= x):
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x,y):
    x_p = find_parent(parent, x)
    y_p = find_parent(parent, y)
    if(x_p<y_p):
        parent[y_p] = x_p
    else:
        parent[x_p] = y_p

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a,b ))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if(find_parent(parent, a)==find_parent(parent, b)):
        continue
    union(parent, a,b)
    res+=cost


print(res)














    

