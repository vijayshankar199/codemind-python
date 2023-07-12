x=input()
l=[]
s=[]
b=["a","A","E","e","i","I","o","O","u","U"]
x=x.split()
for i in x:
    l.append(i)
for i in l:
    c=0
    for j in i:
        if j in b:
            c=c+1
    s.append(c)
print(s.count(min(s)))
    


    