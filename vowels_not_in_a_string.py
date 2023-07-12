x=input()
b=["a","e","i","o","u"]
for i in x:
    if i in b:
        b.remove(i)
if b==[]:
    print(0)
else:
    print(*b)