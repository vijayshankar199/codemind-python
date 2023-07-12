x=input()
l=[]
for i in x:
    if i=="A" or i=="a" or i=="E" or i=="e" or i=="i" or i=="I" or i=="O" or i=="o" or i=="u" or i=="U":
        l.append(i)
if l==[]:
    print(0)
else:
    print(len(l))