for _ in range(int(input())):
    n=int(input())
    b=bin(n)
    b=b[2:]
    print(b.count('1'))