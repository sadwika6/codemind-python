n=int(input())
n=list(str(n))
for i in range(len(n)):
    if n[i]=='6':
        n[i]='9'
        break
print("".join(n))