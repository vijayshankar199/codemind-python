def pal(n):
    k=str(n)
    m=k[::-1]
    if m==k:
        return True
    else:
        return False
        
x=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i)==True:
        c=c+1
print(c)