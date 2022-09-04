n=int(input())
l=list(map(int,input().split()))
m=min(l)
while(m):
    c=0
    for i in l:
        if i%m==0:
            c+=1
    if c==n:
        print(m)
        break
    m-=1