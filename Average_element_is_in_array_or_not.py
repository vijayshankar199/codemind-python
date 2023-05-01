x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in l:
    s=s+i
k=s//x
for i in l:
    if i==k:
        y=y+1
if y==0:
    print(False)
else:
    print(True)