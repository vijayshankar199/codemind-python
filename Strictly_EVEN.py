a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(a):
    if b[i]%2==0 and i%2==0:
        c=c+1
    if b[i]%2==0:
        d=d+1
if c==d:
    print(True)
else:
    print(False)