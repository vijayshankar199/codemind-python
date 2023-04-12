x,y=map(int,input().split())
if x>y:
    mx=x
else:
    mx=y
i=mx
while i>0:
    if i%x==0 and i%y==0:
        print(i)
        break
    i=mx+i