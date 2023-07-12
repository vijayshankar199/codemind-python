x=input()
l1=["a","e","i","o","u"]
l2=["A","E","I","O","U"]
for i in x:
    if i in l1:
        l1.remove(i)
    elif i in l2:
        l2.remove(i)
if l1==[] or l2==[]:
    print(True)
else:
    print(False)