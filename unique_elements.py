a=int(input())
b=list(map(int,input().split()))
c=[]
d=[]
for i in b:
    if i not in c:
        c.append(i)
print(*c)