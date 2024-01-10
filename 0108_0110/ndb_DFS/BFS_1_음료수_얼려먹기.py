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