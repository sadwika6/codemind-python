num=int(input())
sum=0
while(sum!=1 and sum!=4):
    sum=0
    while num>0:
        r=num%10
        sum+=(r*r)
        num=num//10
    num=sum
if sum==1:
    print("True")
else:
    print("False")