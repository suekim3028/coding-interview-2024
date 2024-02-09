# 문제
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
# 이때 이 수열에서 x가 등장하는 횟수를 계산하세요.
# 예를 들어 수열 {1, 1, 2 ,2 ,2 ,2, 3}이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 ‘시간 초과’ 판정을 받습니다.

# 입력 조건
# 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다.
# 1 <= N <= 1,000,000
# 1e9 <= x <= 1e9
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
# 1e9 <= 각 원소의 값 <= 1e9

# 출력 조건
# 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다.
# 단 값이 x인 원소가 하나도 없다면 -1일 출력합니다.

# 입력 예시
# 7 2
# 1 1 2 2 2 2 3

# 7 4
# 1 1 2 2 2 2 3

# 출력 예시
# 4

# -1


import datetime
from bisect import bisect_left, bisect_right


def try1():
    # 2024-02-10 01:24:55.727232
    # 2024-02-10 01:27:47.809481
    
    n, x = map(int, input().split())

    arr = list(map(int, input().split()))

    left = bisect_left(arr, x)
    right = bisect_right(arr, x)

    if(left == right):
        print(-1)
    else:
        print(right-left)

    return
print(datetime.datetime.now())
try1()