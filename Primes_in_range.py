def prime(n):
    if n==1:
        return False
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
        else:
            return True

a=int(input())
b=int(input())
c=0
for n in range(a,b+1):
    if prime(n)==True:
        c=c+1
print(c)