for _ in range(int(input())):
    n=int(input())
    k=-1
    i=1
    while n:
        k+=1
        n=n//2
    print((2**k)-1)
        