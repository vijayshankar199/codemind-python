x=int(input())
c=0
s=0
k=str(x)
m=k[::-1]
n=int(m)

t=x
while n>0:
    r=n%10
    c=c+1
    s=s+(r**c)
    n=n//10
if s==t:
    print(True)
else:
    print(False)
    