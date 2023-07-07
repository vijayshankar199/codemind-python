x=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    s=str(i)
    k=len(s)
    if (i<0):
        k=k-1
    print(k,end=" ")