n=int(input())
print('0','1',end=' ')
a=0
b=1
temp=0
i=0
while i<n-2:
    temp=a+b
    a=b
    b=temp
    print(temp,end=' ')
    i+=1