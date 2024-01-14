from collections import deque;

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
];

visited = [False]* 9;


def dfs(graph, v, visited):
    visited[v] = True;
    print(v, end = ' '),
    for i in graph[v]: # stack으로 하라고 했지만 for 문으로 돌면서 모든 adjacent node에 대해 dfs 함수를 실행-> 자동으로 깊이 우선 하게됨
        if not visited[i]:
            dfs(graph, i , visited);

dfs(graph, 1, visited);
print("")


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
];

visited = [False]* 9;



def bfs(graph, start, visited):
    visited[start] = True;
    queue = deque([start]);
    while queue:
        v = queue.popleft();
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


    

bfs(graph, 1, visited);
