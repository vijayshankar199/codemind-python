x=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        c.append(l[i])
if c==[]:
    print(-1)
else:
    print(min(c))