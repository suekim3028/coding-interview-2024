
def try1():
    n,m,k = map(int, input().split());
    int_list = map(int, input().split());

    max = 1;
    semi_max = 1;

    for i in int_list:
        if(max<=i):
            semi_max = max;
            max=i;

    result=0;

    while(m>=1):
        result+=min(m, k)*max;
        m-=k;
        if(m>=1):
            result+=semi_max;
            m-=1;

    print(result)

def try2():
    n,m,k = map(int, input().split());
    int_list = list(map(int, input().split()));

    int_list.sort(reverse=True);
    max=int_list[0];
    semi_max= int_list[1];

    result = (max * k + semi_max) * (m//(k+1)) + max * (m%(k+1));
    print(result);


try2()