n=int(input())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
c=l1.count(-1)+l2.count(-1)
sl1=sum(l1)+l1.count(-1)
sl2=sum(l2)+l2.count(-1)
if c==2:
    print('Infinite')
else:
    c=0
    for i in range(100):
        if i+sl1==sl2:
            c+=1
    print(c)