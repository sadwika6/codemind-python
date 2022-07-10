n=int(input())
l=list(map(int,input().split()))
c=''
for i in l:
    c+=str(i)
c=int(c,2)
print(c)