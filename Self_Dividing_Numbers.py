a=int(input())
b=int(input())
for i in range(a,b+1):
    c=0
    s=0
    t=i
    while t:
        d=t%10
        s+=1
        t=t//10
        if d==0:
            break
        elif i%d==0:
            c+=1
    if s==c:
        print(i,end=' ')