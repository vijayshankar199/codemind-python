n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if i%2==1:
        c=c+1
if c==0:
    print(True)
else:
    print(False)