def prime(x):
    if x==1:
        pass
    else:
        for i in range(2,int((x**0.5)+1)):
            if x%i==0:
                return False
        else:
            return True
n=int(input())
l=list(map(int,input().split())) 
c=s=0
for i in l:
    if prime(i)==True:
        s=s+i
        c=c+1
print("%.2f" %(s/c))
   