def prime(n):
    if n==1:
        pass
    else:
        for i in range(2,int((n**0.5)+1)):
            if n%i==0:
                return False
        else:
            return True
x=int(input())
y=int(input())
c=0
for i in range(x,y):
    if prime(i)==True:
        print(i)