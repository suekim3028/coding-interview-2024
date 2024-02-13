import datetime
import sys
input = sys.stdin.readline

def try1():
    # 2024-02-13 17:39:51.125595
    # 2024-02-13 17:51:28.821043
    n = int(input())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))
        
    max_arr = [arr[0]]

    for i in range(1, n):
        app = []
        for j in range(i+1):
            max_before = -1
            if(j==0):
                max_before = max_arr[i-1][0]
            elif(j==i):
                max_before = max_arr[i-1][j-1]
            else:
                max_before = max(max_arr[i-1][j-1], max_arr[i-1][j])
            app.append(arr[i][j]+max_before)
        max_arr.append(app)

    print(max(max_arr[-1]))
    return
print(datetime.datetime.now())
try1()


