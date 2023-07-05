x=int(input())
s=set(map(int,input().split()))
l=list(s)
c=0
for i in l:
    c=c+i
print(c)