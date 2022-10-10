def countways(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return countways(n-1)+countways(n-2)+countways(n-3)
n=int(input())
s=countways(n)
print(s)