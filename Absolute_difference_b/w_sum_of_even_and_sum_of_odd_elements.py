n=int(input())
l=list(map(int,input().split()))
o=0
s=sum(l)
for i in l:
    if i%2!=0:
        o+=i
e=s-o
print(abs(e-o))