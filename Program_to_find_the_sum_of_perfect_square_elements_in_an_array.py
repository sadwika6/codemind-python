def perfect(n):
    for i in range(n+1):
        if i*i==n:
            return n
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
t=0
for i in a:
    s=perfect(i)
    t+=s
print(t)