def prime(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return 0;
    else:
        return 1;
a=int(input())
b=int(input())
if a==1:
    a=2;
for i in range(a,b+1):
    if(prime(i)):
        print(i)