a=int(input())
s=0
for i in range(1,a):
    if(i*i==a):
        s+=1
        break
if s==1:
    print('True')
else:
    print('False')