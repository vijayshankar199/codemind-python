x=int(input())
l=list(map(int,input().split()))
s=0
for i in l:
    s=s+i
k=s/x
print("%0.2f" %k)