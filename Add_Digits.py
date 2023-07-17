x=int(input())
k=0
while x>0:
    r=x%10
    k=k+r
    x=x//10
    if k>9 and x==0:
        x=k
        k=0
else:
    print(k)
    