x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in range(0,len(l)):
    if l[i]%2==1:
        s=s+l[i]
print(s)