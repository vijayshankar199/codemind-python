x=input().split()
l=[]
for i in x:
    k=i[::-1]
    l.append(k)
print(*l)