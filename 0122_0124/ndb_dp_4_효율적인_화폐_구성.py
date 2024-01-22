# 문제
# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 예를 들어 2원, 3원 단위의 화폐가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

# 입력 조건
# 첫째 줄에 N,M이 주어진다(1<= N <= 100, 1<= M <= 10,000)
# 이후의 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.

# 출력 조건
# 첫째 줄에 경우의 수 X를 출력한다.
# 불가능할 때는 -1을 출력한다.

# 입력 예시
# 2 15
# 2
# 3

# 3 4
# 3
# 5
# 7

# 출력 예시
# 5

# -1
 

import datetime


def try1():
    # 2024-01-22 23:57:01.457650
    # 2024-01-23 00:19:34.936072
    i,j = map(int, input().split())
    currency = []
    for _i in range(i):
        currency.append(int(input()))

    currency = sorted(currency)

    if(j < currency[0]):
        print(-1)
        return
    
    # 2, 3 , 5

        

    arr = [-1]*(j+1)
    def getValue(k,x):
        if(k in currency):
            return 1
        if(k>x):
            value = arr[k-x]
            return value+1 if value!=-1 else -1
        else:
            return -1

    for k in range(currency[0], j+1):
        _possible = map(lambda x: getValue(k,x), currency)
        possible = list(filter(lambda x: x!=-1, _possible))

        arr[k] = -1 if len(possible)==0 else min(possible)

    print(arr[j])
    
print(datetime.datetime.now())
try1()