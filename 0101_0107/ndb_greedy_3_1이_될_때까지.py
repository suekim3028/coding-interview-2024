def try1():
    n,k = map(int, input().split());
    result = 0;
    
    while(n>1):
        result +=  (n%k +1);
        n = n//k;

    print(result);


try1();