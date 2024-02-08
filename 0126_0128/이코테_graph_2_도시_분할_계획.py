# 동물원에서 막 탈출한 원숭이 한 마리가 세상 구경을 하고 있다. 어느 날 원숭이는 '평화로운 마을'에 잠시 머물렀는데 마침 마을 사람들은 도로 공사 문제로 머리를 맞대고 회의 중이었다.

# 마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있는 편리한 길이다. 그리고 길마다 길을 유지하는데 드는 유지비가 있다.

# 마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다. 마을이 너무 커서 혼자서는 관리할 수 없기 때문이다. 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다. 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻이다. 마을에는 집이 하나 이상 있어야 한다.

# 그렇게 마을의 이장은 계획을 세우다가 마을 안에 길이 너무 많다는 생각을 하게 되었다. 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있다. 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있다. 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶다. 이것을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 집의 개수 N, 길의 개수 M이 주어진다. N은 2 이상 100,000 이하인 정수이고, M은 1 이상 1,000,000 이하인 정수이다.
# 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A, B, C 3개의 정수로 공백으로 구분되어 주어지는데 A번 집과 B번 집을 연결하는 길의 유지비가 C(1 <= C <= 1,000) 라는 뜻이다.

# 출력
# 첫째 줄에 길을 없애고 남은 유지비 합의 최솟값을 출력한다.

# 입력 예시
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

# 출력 예시
# 8

import datetime


def find_p(parent,a):
    if(parent[a] != a):
        parent[a]=find_p(parent,parent[a])
    return parent[a]

def union(parent, a, b):
    a_p = find_p(parent, a)
    b_p = find_p(parent, b)
    
    if(a_p<b_p):
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p
    

def try1():
    # 2024-02-08 23:10:16.961838
    # 2024-02-09 00:15:22.713353

    # 두개의 spanning tree 로 나누기
    # 간선 cost 순으로 정렬해서 앞부터 둘 사이에 사이클 없으면 (parent가 같지 않으면) 포함시키고 union
    # spanning tree 에서 간선 하나 빼면 두개의 spanning tree 됨

    n, m = map(int, input().split())

    edges = []
    parent = []

    for i in range(n+1):
        parent.append(i)

    for _ in range(m):
        a, b, cost = map(int, input().split())
        edges.append((cost,a,b))

    edges.sort()
    res = 0
    last = 0


    print(edges)

    for edge in edges:
        cost,a,b = edge
        if(find_p(parent,a) != find_p(parent,b)): # 사이클 없으면
            union(parent,a,b)
            res+=cost
            last = cost
        
    print(res-last)
    return


print(datetime.datetime.now())
try1()