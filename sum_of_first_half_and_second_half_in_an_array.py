n=int(input())
l=list(map(int,input().split()))
f=s=0
k=len(l)//2
for i in range(k):
    f=f+l[i]
for j in range(k,len(l)):
    s=s+l[j]
print(f)
print(s)