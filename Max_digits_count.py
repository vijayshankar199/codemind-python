a=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    k=str(i)
    m=len(k)
    s.append(m)
f=max(s)
c=s.count(f)
print(c)