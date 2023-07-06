a,b=map(int,input().split())
l=list(map(int,input().split()))
s=list(map(int,input().split()))
c=[]
e=[]
for i in l:
    for j in s:
        if i==j:
            if j not in c:
                c.append(j)
        
print(*c) 