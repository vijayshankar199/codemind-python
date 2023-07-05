n=int(input())
l=list(map(int,input().split()))
a=int(input())
sum=0
for i in range(len(l)):
    if i==a:
        break
    else:
        sum=sum+l[i]
print(sum)