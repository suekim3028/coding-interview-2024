import datetime


import sys

input = sys.stdin.readline

def try1():
    # 2024-02-10 18:40:58.351197
    # 2024-02-10 18:57:11.996926
    # 2024-02-10 19:40:17.868448
    # 2024-02-10 20:34:01.290853

    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    print(arr[int((n-1)//2)])


print(datetime.datetime.now())
try1()
