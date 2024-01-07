def try1():
    n, m = map(int, input().split());


    result = 1;
    for _i in range(n):
        row = list(map(int, input().split()));
        row.sort(); # min 만 가져와도 됨
        
        result = max(result, row[0]);

    print(result);




try1();