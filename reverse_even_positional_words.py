x=input().split()
l=[]
z=[]
for i in x:
    l.append(i)

for i in range(len(l)):
    if i%2==0:
        k=l[i]
        m=k[::-1]
        z.append(m)
    else:
        z.append(l[i])
print(*z)