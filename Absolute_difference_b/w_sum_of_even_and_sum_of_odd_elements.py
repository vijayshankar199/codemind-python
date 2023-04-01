x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in l:
    if i%2==0:
        s=s+i
    else:
        y=y+i
print(abs(s-y))