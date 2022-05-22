def prime(x):
    for i in range(2,x//2+1):
        if(x%i==0):
            return 0
    else:
        return 1
n1=int(input())
n2=int(input())
n=n1+n2
i=1
while(True):
    x=n+i
    if prime(x):
        print(i)
        break
    i+=1