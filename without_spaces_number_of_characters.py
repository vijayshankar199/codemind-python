x=input().split()
l=[]
for i in x:
    k=i[::-1]
    m=len(k)
    l.append(m)
print(sum(l))