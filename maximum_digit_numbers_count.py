a=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    k=str(i)
    m=len(k)
    s.append(m)
for i in l:
    if len(str(i))==max(s):
        print(i,end=" ")