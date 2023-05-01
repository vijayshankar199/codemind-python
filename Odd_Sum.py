x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in l:
    if i%2==1:
        s=s+i
print(s)