l=list(map(str,input().split()))
v="aeiouAEIOU"
c=0
for i in l:
    for j in range(len(i)):
        if i[0] in v and i[len(i)-1] not in v:
            c=c+1
            break
print(c)