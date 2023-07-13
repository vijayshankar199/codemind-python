l=list(map(str,input().split()))
f=l[0]
d=l[len(l)-1]
z=[]
c=[]
for i in range(len(f)):
    z.append(ord(f[i]))
for i in range(len(d)):
    c.append(ord(d[i]))
print(chr(min(z)),chr(max(c)))