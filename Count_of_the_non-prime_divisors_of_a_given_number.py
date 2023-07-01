def prime(x):
    if x==1:
        return False
    else:
        for j in range(2,int((i**0.5)+1)):
            if i%j==0:
                return False
        else:
            return True
    
x=int(input())
c=0
for i in range(1,x+1):
    if x%i==0:
        if prime(i)==False:
            c+=1
print(c)
            