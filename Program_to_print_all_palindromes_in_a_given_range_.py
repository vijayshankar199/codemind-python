def pal(n):
    k=str(n)
    if k==k[::-1]:
        return True
x=int(input())
y=int(input())
for i in range(x,y):
    if pal(i)==True:
        print(i,end=" ")