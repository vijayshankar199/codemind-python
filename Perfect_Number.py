x=int(input())
s=0
for i in range(1,x):
    if x%i==0:
        s+=i
if x==s:
    print(True)
else:
    print(False)