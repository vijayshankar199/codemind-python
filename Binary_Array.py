n=int(input())
l=list(map(int,input().split()))
max(l)
if max(l)==1 or max(l)==0:
    print(True)
else:
    print(False)