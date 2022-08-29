n=int(input())
s=input()
k=s.count('.')
if k>n//2:
    print('YES')
    a=s.replace('.','B')
    print(a)
else:
    print('NO')