def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
a,b,c,d=map(int,input().split())
i=a
j=c
f1=0
f2=0
k=True
for i in range(a,b+1):
    f1=0
    for j in range(c,d+1):
        k=prime(i+j)
        if(k==False):
            f1+=1
        if f1==(d-c+1):
            print('Takahashi')
            f2=1
            break
    if f2==1:
        break
else:
    print('Aoki')