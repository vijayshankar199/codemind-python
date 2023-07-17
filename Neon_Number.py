x=int(input())
n=x*x
k=n
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
if x==s:
    print("Neon Number")
else:
    print("Not Neon Number")