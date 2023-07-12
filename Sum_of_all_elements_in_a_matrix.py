a,b=map(int,input().split())
c=[]
s=o=0
for i in range(a):
    l=list(map(int,input().split()))
    c.append(l)
for i in range(a):
    for j in range(b):
        s=s+c[i][j]
print(s)