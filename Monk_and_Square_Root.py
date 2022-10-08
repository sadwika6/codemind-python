for _ in range(int(input())):
    a,b=map(int,input().split())
    f=0
    for i in range(b):
        if (i*i)%b==a:
            f=1
            print(i)
            break
    if f==0:
        print(-1)