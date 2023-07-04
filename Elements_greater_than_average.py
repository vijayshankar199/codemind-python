n=int(input())
l=list(map(int,input().split()))
k=(sum(l)//n)
c=0
for i in l:
    if i>=k:
        c=c+1
print(c)