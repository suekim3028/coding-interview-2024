# 문제
# 고정점(Fixed Point)이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
# 예를 들어 수열 a = {-15, -4, 2, 8, 13}이 있을 때 a[2] = 2이므로, 고정점은 2가 됩니다.
# 하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다.
# 이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요.
# 고정점은 최대 1개만 존재합니다.
# 만약 고정점이 없다면 1을 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과'판정을 받습니다.

# 입력 조건
# 첫째 줄에 N이 입력됩니다. (1 <= N <= 1,000,000)
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10의 9승 <= 각 원소의 값 <= 10의 9승)

# 출력 조건
# 고정점을 출력한다.
# 고정점이 없다면 -1을 출력합니다.

# 입력 예시
# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15

# 출력 예시
# 3
# 2
# -1

import datetime
import bisect
import sys

input =sys.stdin.readline

def try1():
    # 2024-02-13 17:23:23.962132
    # 2024-02-13 17:36:04.067064

    INF = int(10e9)+1

    n = int(input())
    arr = list(map(int, input().split()))
# -15 -4 3 8 9 13 15

    left = 0
    right = n-1
    middle = (left+(right-left)//2)

    # 0 1 2 3 4
    
    res = -1
    while(res == -1 and left<right and left!=middle and right!=middle):
        if(arr[middle]<middle):
            left = middle
            middle = (left+(right-left)//2)
        elif(arr[middle]>middle):
            right = middle
            middle = (left+(right-left)//2)
        else:
            res = middle

    if(res==-1):
        if(arr[right]==right):
            print(res)
        elif(arr[left]==left):
            print(left)
        else:
            print(-1)
    else:
        print(res)

    return
print(datetime.datetime.now())
try1()