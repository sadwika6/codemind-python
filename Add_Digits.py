a=int(input())
s=0
s1=0
while a>0:
    r=a%10
    s+=r
    a=a//10
    if a==0 and s>9:
        a=s
        s=0
print(s)        