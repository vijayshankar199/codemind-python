x=int(input())
l=list(map(int,input().split()))
s=y=0
for i in range(len(l)-1,-1,-1):
    if l[i]%2==0:
        print(i)
        break