a,b,c=map(int,input().split())
c=2*a*b*c*512
m="KB"
k=c//1024
print(str(k)+m)