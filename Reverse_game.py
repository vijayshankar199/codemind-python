def pal(n):
    k=str(n)
    m=str(k[::-1])
    z=int(m)
    return z
c=[]   
x=int(input())
l=list(map(int,input().split()))

for i in l:
    pal(i)
    c.append(pal(i))
print(*c)