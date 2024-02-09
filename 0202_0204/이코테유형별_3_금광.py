# 문제
# n x m 크기의 금광이 있습니다.

# 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.

# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다.

# 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다.

# 이후에 m - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.

# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

# 만약 다음과 같이 3 x 4 크기의 금광이 존재한다고 가정합시다.

#   1 3 3 2
#   2 1 4 1
#   0 6 4 7
# 가장 왼쪽 위의 위치를 (1, 1), 가장 오른쪽 아래의 위치를 (n, m)이라고 할 때,

# 위 예시에서는 (2, 1) → (3, 2) → (3, 3) → (3, 4)의 위치로 이동하면 총 19만큼의 금을 채굴할 수 있으며, 이때의 값이 최댓값입니다.

# 입력 조건
# 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
# 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20)
# 둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)
# 출력 조건
# 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
# 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
# 입력 예시
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
# 출력 예시
# 19
# 16

import datetime
import sys
import itertools

input = sys.stdin.readline

def try1():
    # 2024-02-10 01:39:53.095274
    # 2024-02-10 02:23:35.527128

    t = int(input())
    res = []

    for _ in range(t):
        n, m = map(int,input().split())

        graph = list(map(int,input().split()))
        arr = [graph[j::m] for j in range(m)]

        # 해당 셀로 왔을때 내 왼쪽 위, 왼쪽, 왼쪽 아래 중 max 랑 더함
        
        memo = []

        for i in range(m):
            if(i == 0):
                memo.append(arr[0])
                
                continue
            else:
                to_append = []
                for j in range(n):
                    max_gold = max(memo[i-1][max(j-1,0):j+2]) + arr[i][j]
                    to_append.append(max_gold)
                memo.append(to_append)

        
        res.append(max(memo[m-1]))
    for i in res:
        print(i)
    return
print(datetime.datetime.now())
try1()