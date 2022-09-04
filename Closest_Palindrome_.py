def pl(n):
    s=str(n)
    s=s[::-1]
    n1=int(s)
    if n1==n:
        return True
    else:
        return False
n=int(input())
for i in range(n-1,0,-1):
    if pl(i):
        bf=i
        break
i=n+1
while True:
    if pl(i):
        af=i
        break
    i+=1
if n-bf==af-n:
    print(bf,af)
elif n-bf<af-n:
    print(bf)
else:
    print(af)