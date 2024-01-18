# 오늘 동빈이는 여행 가신 부모님을 대신해서 떡집 일을 하기로 했다. 오늘은 떡볶이 떡을 만드는 날이다. 
# 동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않다. 
# 대신에 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
# 절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다. 
# 높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않는다.
# 예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기를 높이를 15cm로 지정하면 자른 뒤 떡의 높이는 15, 14, 10, 15cm가 될 것이다. 잘린 떡의 길이는 차례대로 4, 0, 0, 2cm 이다, 손님은 6cm만큼의 길이를 가져간다.
# 손님이 왔을 때 요청한 총 길이가 M일때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

# 입력조건
# 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1000000, 1 <= M <= 2000000000)
# 둘째 줄에는 떡의 개별 높이가 주어진다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.

# 출력조건
# 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

# 입력 예시
# 4 6
# 19 15 10 17

# 출력 예시
# 15
 
import datetime

# 이진탐색에서 같은 수가 아닌 크거나 작은 수 찾는 연습
def try1():
    # 2024-01-19 00:12:59.501282
    # 2024-01-19 00:08:25.629532
    
    i,j = map(int, input().split())
    arr = list( map(int, input().split()))

    # h 보다 큰 *첫번째* 인덱스 찾기

    arr= sorted(arr)
    h = arr[i-1]-1 # 18


    # 10 15 17 19
    
    while(h>=1):        
        start = 0;
        end = i-1; 
        target = h+1
        while(start<end):
            mid = start + (end-start)//2
            if(mid == start or end ==start): break
            
            if(arr[mid]>target):
                end = mid
            else: # arr[mid]<=target
                start = mid

        index= start if arr[start]>=target else end

        if(j<=sum(arr[index:]) - h*(i-index)):
            break
        else:
            h-=1
    
    print(h)

print(datetime.datetime.now())
try1()