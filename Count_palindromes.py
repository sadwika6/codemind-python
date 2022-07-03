n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    k=str(abs(i))
    if k==k[::-1]:
        c+=1
print(c)