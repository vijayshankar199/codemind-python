n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
h=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        h.append(i)
if len(h):
    print(max(h))
else:
    print(-1)