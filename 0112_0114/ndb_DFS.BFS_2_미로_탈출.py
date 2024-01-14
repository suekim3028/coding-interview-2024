# 문제
# 동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

# 입력 조건
# 첫째 줄에 두 정수 N, M (4 ≤ N,M ≤ 200)이 주어집니다. 다음 N개의 줄에는 각각 M개의 정수(0 또는 1)로 미로의 정보가 주어진다. 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한 시작 칸과 마지막 칸은 항상 1이다.

# 출력 조건
# 첫째 줄에 최소 이동 칸의 개수를 출력한다.

# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10
from collections import deque
# 2024-01-14T10:55:52.208Z
def try1():
    n,m = map(int, input().split())
    board = []
    visited=[]
    for _i in range(n):
        row = list(map(int, list(input())));
        board.append(row)
        visited.append([0 if x == 1 else 1 for x in row]);

    # 아래나 오른쪽으로 무조건 가고 없는 경우만 위 혹은 왼쪽으로 가야함?
    
    def bfs(graph,  visited):
        visited[0][0] = True
        queue = deque([(0,0)])
        res = 1
        while(queue):
            curr_row, curr_col = queue.popleft()
            print(curr_row, curr_col)
            if(curr_row == n-1 and curr_col == m-1):
                break

            for i,j in [(curr_row, curr_col+1),(curr_row+1, curr_col), (curr_row,curr_col-1), (curr_row-1,curr_col)]:
                if(i>=n or j>=m or visited[i][j]==True):
                    continue
                else:
                    queue.append((i,j))
                    visited[i][j] = True
                    res+=1
                    break
        return res
    
    print(bfs(board,  visited))

try1()