# 문제
# N × M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하라.
# 다음의 4 × 5 얼음 틀 예시에서는 아이스크림이 총 3개가 생성된다


# 입력
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1,000)
# 두 번째 줄부터 N + 1 번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
# 출력
# 한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

# 입력 예시 1

# 4 5
# 00110
# 00011
# 11111
# 00000
# 출력 예시 1

# 3

def try1():

    n,m = map(int,input().split());
    board = []
    visited = []

    for _i in range(n):
        board.append(list(map(int,list(input()))));
        visited.append([0]*m);

    def connect(row, col):
        visited[row][col] =1;
        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            next_row = row+dr;
            next_col = col + dc;

            if((0<=next_row<n) and (0<=next_col<m) and visited[next_row][next_col] == 0 and board[next_row][next_col] == 0):
                visited[next_row][next_col] = 1;
                connect(next_row, next_col)

    res=0;
    for i in range(n):
        for j in range(m):
            if(visited[i][j] == 0 and board[i][j]==0):
                connect(i, j)             
                res+=1;
    print(res);

try1()