n=int(input())
a=list(map(int,input().split()))
m=max(a)
t=int(input())
for i in a:
    if i+t>=m:
        print("True",end=' ')
    else:
        print("False",end=' ')