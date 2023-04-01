x=int(input())
l=list(map(int,input().split()))
z=int(input())
s=0
for i in l:
    if i==z:
        s=s+1
if s==0:
    print(False)
else:
    print(True)