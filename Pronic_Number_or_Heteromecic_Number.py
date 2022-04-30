n=int(input())
i=1
h=0
while i<n:
    if i*(i+1)==n:
        h=1
    i+=1
if h==1:
    print("YES")
else:
     print("NO")