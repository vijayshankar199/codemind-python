def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
y=int(input())
s=x+y
k=s
m=s+1
while m>0:
    if prime(m)==True:
        break
    else:
        m=m+1
print(abs(k-m))