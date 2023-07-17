def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True
x=int(input())
c=0
for i in range(1,x+1):
    if x%i==0:
        if prime(i)==False:
            c=c+1
print(c+1)