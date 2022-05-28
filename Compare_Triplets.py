a=list(map(int,input().split()))
b=list(map(int,input().split()))
al=0
bo=0
for i in range(3):
    if a[i]>b[i]:
        al+=1
    if a[i]<b[i]:
        bo+=1
print(al,bo)