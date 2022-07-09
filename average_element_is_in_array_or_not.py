n=int(input())
l=list(map(int,input().split()))
s=sum(l)
k=s//n
if k in l:
    print(True)
else:
    print(False)