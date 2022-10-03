for _ in range(int(input())):
    s=input()
    n=int(s,16)
    b=bin(n)
    res=b[2:]
    if len(res)%4!=0:
        k=4-(len(res)%4)
        for i in range(k):
            res='0'+res
    print(res)