import datetime
# 성적이 낮은 순서로 학생 출력하기
# 문제
# N명의 학생의 성적 정보가 주어진다. 형식은 이름 성적 으로 주어지는데 이때 이들의 성적이 낮은 순으로 학생 이름을 출력하는 문제다.

# 입력
# 첫 번째 줄에 학생의 수 N이 입력된다. (1 <= N <= 100,000)
# 두 번째 줄 부터 N+1 번째 줄 까지 학생의 이름 그리고 성적이 공백으로 주어진다. 학생이름 길이는 100이하, 성적은 100이하 자연수로 주어진다.
# 출력
# 모든 학생의 이름을 성적이 낮은 순으로 출력하면된다. 동일한 성적은 자유롭게 출력하면된다.
# 입력 예시

# 2
# 홍길동 96
# 이순신 78
# 출력 예시

# 이순신 홍길동

# TODO: ?? 맨 마지막에 한번만 출력하면 됨 -> 한번 sort 하면 되잖아요

def try1():
    # 2024-01-14 20:41:09.646993
    # 2024-01-14 20:45:35.156005
    print(datetime.datetime.now())

    n = int(input())
    student, _grade = input().split()
    grade = int(_grade)

    res = []

    res.append([student, grade])
    for _i in range(n-1):
        student, _grade = input().split()
        grade = int(_grade)
        inserted = False
        for j in range(len(res)):
            if(res[j][1]>=grade):
                res.insert(j, [student, grade])
                inserted = True
                break
        if not inserted:
            res.append([student, grade])
    
    for i,j in res:
        print(i, end= " ")


def try2():
    n= int(input())
    res = [];
    for _i in range(n):
        student, _grade = input().split();
        grade = int(_grade)
        res.append((student, grade));
    res.sort(key= lambda x:x[1])

    for student, _grade in res:
        print(student, end = ' ')

try2()