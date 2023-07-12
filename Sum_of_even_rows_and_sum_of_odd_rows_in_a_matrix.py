a,b=map(int,input().split())
c=[]
s=o=0
for i in range(a):
    l=list(map(int,input().split()))
    c.append(l)
for i in range(a):
    for j in range(b):
        if i%2==0:
            s=s+c[i][j]
        else:
             o=o+c[i][j]
print(s,o)