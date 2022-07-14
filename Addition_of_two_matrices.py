n=int(input())
m1=[]
m2=[]
for i in range(n):
    l1=list(map(int,input().split()))
    m1.append(l1)
for i in range(n):
    l2=list(map(int,input().split()))
    m2.append(l2)
for i in range(n):
    for j in range(n):
        m1[i][j]+=m2[i][j]
for i in range(n):
    for j in range(n):
        if j==n-1:
            print(m1[i][j],end='
')
        else:
            print(m1[i][j],end=' ')