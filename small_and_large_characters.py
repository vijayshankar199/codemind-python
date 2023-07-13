def st(n):
    l=[]
    for i in range(len(n)):
        l.append(ord(n[i]))
    print(chr(min(l)),chr(max(l)),end=" ")
x=input().split()
k=[]
for i in x:
    k.append(i)
    
for i in k:
    st(i)