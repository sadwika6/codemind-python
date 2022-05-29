t=int(input())
for i in range(t):
    s=input()
    x=''.join(reversed(s))
    if s!=x:
        print("NO")
    elif s==x and len(s)%2==0:
        print("YES EVEN")
    elif s==x and len(s)%2!=0:
        print("YES ODD")