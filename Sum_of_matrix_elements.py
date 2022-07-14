a=int(input())
m1=[]
b=int(input())
for i in range(a):
    l1=list(map(int,input().split()))
    m1.append(l1)
s=0
for i in m1:
    s+=sum(i)
print(s)