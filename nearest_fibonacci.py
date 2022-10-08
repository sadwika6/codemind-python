n=int(input())
a=0
b=1
for i in range(n):
    c=a+b
    a=b
    b=c
    if b>n:
        if abs(n-a)<abs(n-b):
            print(a)
            break
        elif abs(n-a)>abs(n-b):
            print(b)
            break
        else:
            print(a,b)
            break