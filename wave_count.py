n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,n-2,2):
    if l[i]<l[i+1]:
        c+=1
    else:
        c=0
        print(-1)
        break
if c!=0:
    print(c)