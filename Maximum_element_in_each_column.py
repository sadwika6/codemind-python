a,b=map(int,input().split())
m1=[]
for i in range(a):
    l1=list(map(int,input().split()))
    m1.append(l1)
for j in range(b):
    m=0
    for i in range(a):
        if m1[i][j]>m:
            m=m1[i][j]
    print(m)