n=int(input())
s=0
a=n
while a>0:
    i=1
    fact=1
    r=a%10
    while i<=r:
        fact=fact*i
        i+=1
    s+=fact
    a=a//10
if(n==s):
    print("The number",n,"is a strong number")
else:
    print("The number",n,"is not a strong number")