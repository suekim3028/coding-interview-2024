# 문제
# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개의 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
# 예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

# N=5
# [8, 3, 7, 9, 2]
# 손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

# M=3
# [5, 7, 9]
# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.

# 입력
# 첫째 줄에 정수 N이 주어진다. (1<=N<=1,000,000)
# 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
# 셋째 줄에는 정수 M이 주어진다. (1<=M<=100,000)
# 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.
# 출력
# 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
# 입력 예시

# 5
# 8 3 7 9 2
# 3
# 5 7 9
# 출력 예시

# no yes yes
 
import sys
import datetime


# input_data = sys.stdin.readline().rstrip()

# 개수가 1000만 이상이거나 범위가 1000억 이상이면 이진탐색 고려
# TODO: 계수정렬 or set으로 풀어보기
def try1():
    # 2024-01-18 23:52:45.616125
    # 2024-01-19 00:08:25.629532
    i = int(input())
    a = list(map(int, input().split()));
    j = int(input());
    b = list(map(int, input().split()));

    a = sorted(a);

#   2 3 7 8 9

    def find(num, start, end):
        middle = start + (end-start)//2

        start_num = a[start];
        end_num = a[end];
        middle_num = a[middle];

        if(middle<= start or middle>=end):
            return start_num == num or end_num==num;

        if(middle_num== num): 
            return True
        elif (middle_num>num):
            return find(num, start, middle);
        else:
            return find(num, middle, end);
    
    for num in b :
        found = find(num, 0, i-1)
        print("yes" if found else "no" , end = " ",)


print(datetime.datetime.now())
try1()