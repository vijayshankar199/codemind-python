x=int(input())
s=set(map(int,input().split()))
l=list(s)
c=0
for i in l:
    if i%2==1:
        c=c+1
print(c)