def prime(x):
    for i in range(2,int((x**0.5)+1)):
            if x%i==0:
                return False
    else:
        return True
def revprime(m):
    for i in range(2,int((m**0.5)+1)):
            if m%i==0:
                return False
    else:
        return True
x=int(input())

c=x
e=str(x)
t=str(e[::-1])
m=int(t) 
if prime(x)==True:
    if revprime(m)==True:
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")