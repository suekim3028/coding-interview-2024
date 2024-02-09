import datetime
import sys

    

def try1():
    # 2024-02-10 01:10:57.160985
    # 2024-02-10 01:17:08.912941

    input = sys.stdin.readline

    n = int(input())

    arr = []

    for _ in range(n):
        name, _kor, _eng, _mat =  input().split()
        kor, eng, mat = map(int, [_kor, _eng, _mat])
        arr.append((name, kor, eng, mat))
    arr = sorted(arr, key = lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in arr:
        print(i[0])

    return
    
print(datetime.datetime.now())
try1()
