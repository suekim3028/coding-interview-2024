# 문제
# 정수 X가 주어질때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
# 1) X가 5로 나누어떨어지면, 5로 나눈다.
# 2) X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3) X가 2로 나누어 떨어지면, 2로 나눈다.
# 4) X에서 1을 뺀다.
# 정수 X가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들어야한다. 이 연산을 사용하는 횟수의 최솟값을 출력해라.

# X = 26일 경우
# 1. 26 - 1 = 25
# 2. 25 /5 = 5
# 3. 5 / 5 = 1

# 입력
# 첫째 줄에 정수 X이 주어진다. (1<=X<=30,000)
# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
# 입력 예시

# 26
# 출력 예시

# 3
 
import sys
import datetime


# input_data = sys.stdin.readline().rstrip()

def try1():
    # 2024-01-22 00:06:44.553663
    # 2024-01-22 00:23:54.053940

    i = int(input())

    arr = [0]*30001
    
    arr[0]= -1

    for _j in range(30000):
        j =  _j+1

        min2 = arr[int(j/2)] if j%2 ==0 else arr[int(j-1)]
        min3 = arr[int(j/3)] if j%3 ==0 else arr[int(j-1)]
        min5 = arr[int(j/5)] if j%5 ==0 else arr[int(j-1)]
        min1 = arr[int(j-1)]
        minValue = min(min2, min3, min5, min1)
        arr[j] = minValue+1

    print(arr[i])


print(datetime.datetime.now())
try1()