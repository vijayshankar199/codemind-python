x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in range(0,len(l)-1):
    if l[i]%2==0:
        s=s+l[i]
print(s)