n=int(input())
b=[]
s=0
for i in range(n):
    a=int(input())
    b.append(a)
t=int(input())
for i in b:
    if(i<=t):
        s+=1
    else:
        s+=2
print(s)