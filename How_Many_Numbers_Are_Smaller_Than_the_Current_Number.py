n=int(input())
a=list(map(int,input().split()))
for i in a:
    d=0
    for j in a:
        if j<i:
            d+=1
    print(d,end=' ')