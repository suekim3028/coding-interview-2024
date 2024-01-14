# 위에서 아래로
# 문제
# 하나의 수열에는 다양한 수가 존재하며, 이런 큰 수는 크기와 상관 없이 무작위로 주어진다. 이 수를 큰수 부터 작은 수까지 내림차순으로 정렬하면되는 문제다. 즉 수열을 내림차순으로 정렬하는 프로그램을 만들면된다.

# 입력
# 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. 이때 범위는 1 <= N <= 500
# 둘째 줄부터 N + 1 번째 줄 까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하 자연수
# 출력
# 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분해서 출력하면된다. 동일한 수는 순서상관없다.
# 입력 예시

# 3
# 15
# 27
# 12

# 출력 예시
# 27 25 12

def try1():
    res = [];
    n = int(input())
    res.append(int(input()));

    for _i in range(n-1):
        v = int(input())
        inserted = False
        for j in range(len(res)):
            if(res[j]<=v):
                res.insert(j, v);
                inserted=True
                break

        if not inserted:
            res.append(v)

    print(res);

try1()