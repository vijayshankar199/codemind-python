l=list(map(str,input().split()))
m=[]
m.append(l[0])
m.append(l[len(l)-1])
f=m[0]
z=[]
c=[]
d=m[1]
for i in range(len(f)):
    z.append(ord(f[i]))
for i in range(len(d)):
    c.append(ord(d[i]))

print(chr(min(z)),chr(max(c)))