def lcm(a,b):
    i=max(a,b)
    while True:
        if i%a==0 and i%b==0:
            break
        else:
            i+=max(a,b)
    return i
n=int(input())
l=list(map(int,input().split()))
m=lcm(l[0],l[1])
for i in range(2,n):
    m=lcm(m,l[i])
print(m)