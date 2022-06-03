t=int(input())
f=0
for i in range(t):
    s=input()
    f=0
    for i in s:
        if i.isdigit():
            f+=1
    if f==len(s):
        print("True")
    else:
        print("False")