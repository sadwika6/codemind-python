n=int(input())
m1=[]
s1=0
s2=0
for i in range(n):
    l1=list(map(int,input().split()))
    m1.append(l1)
for i in range(n):
    for j in range(n):
        if(i==j):
            s1+=m1[i][j]
        if(i+j==n-1):
            s2+=m1[i][j]
print('Principal Diagonal:',end='')
print(s1)
print('Secondary Diagonal:',end='')
print(s2)