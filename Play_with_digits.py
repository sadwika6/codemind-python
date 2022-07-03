n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    while(i):
        r=i%10
        c+=r
        i=i//10
print(c)