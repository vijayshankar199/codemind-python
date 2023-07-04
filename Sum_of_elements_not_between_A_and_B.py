n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
r=0
for i in l:
    if i<a or i>b:
        r=r+i
print(r)