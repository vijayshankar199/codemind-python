n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
r=0
for i in l:
    if i<a or i>b:
        m.append(i)
if len(m):
    print(*m)
else:
    print(-1)