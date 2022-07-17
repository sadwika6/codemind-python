n=int(input())
l=list(map(int,input().split()))
c=0
d=0
for i in range(0,n-1,2):
    if l[i]>l[i+1]:
        c+=1
    elif l[i]<l[i+1]:
        d+=1
if c==0 or d==0:
    print('yes')
else:
    print('no')