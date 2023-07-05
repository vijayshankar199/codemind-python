def prime(x):
    if x==1:
        pass
    else:
        for i in range(2,int((x**0.5)+1)):
            if x%i==0:
                return False
        else:
            return True
x=int(input())
c=0
l=list(map(int,input().split()))
for j in l:
    if prime(j)==True:
        c=c+1
print(c)