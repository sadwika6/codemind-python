n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    i=i**2
    b.append(i)
print(*sorted(b))