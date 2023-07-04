n1=int(input())
n2=int(input())
s=n1+n2
k=s
def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    else:
        return True
m=s+1
while m>0:
    if prime(m)==True:
        break
    else:    
        m=m+1
print(abs(k-m))
