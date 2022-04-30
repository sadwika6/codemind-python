n=int(input())
rev=0
temp=n
if temp>0:
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
    print(rev)
if(temp<0):
    num=abs(n)
    rev=0
    while(num>0):
        r=num%10
        rev=(rev*10)+r
        num=num//10
    print(-rev)