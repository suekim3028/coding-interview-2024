# 문제 정의

# 알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
# 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출련한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 입력
# 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

# 출력
# 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

# 예제 입력 1
# K1KA5CB7

# 예제 출력 1
# ABCKK13

import datetime
from collections import deque

def try1():
    # 2024-02-10 03:29:08.402417
    # 2024-02-10 03:37:58.237737

    q = deque()
    string = list(input())
    string.sort()
    q.extend(string)

    num = 0
    while(q):
        i = q.popleft()
        if(i.isnumeric()):
            num += int(i)
        else:
            q.appendleft(i)
            break
    
    q.append(str(num))
    print("".join(q))
    return
print(datetime.datetime.now())
try1()