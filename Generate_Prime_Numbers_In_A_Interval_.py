def prime(n):
    if n==1:
        pass
    else:
        for i in range(2,int((n**0.5)+1)):
             if n%i==0:
                break
        else:
            print(n)
a=int(input())
b=int(input())
for j in range(a,b):
    prime(j)
    