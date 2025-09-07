l=[2,3,4,3,2,5,5]
d={}
s=0
for i in range(len(l)):
    if len(d)==len(l)+1//2:
        break
    if l[i] not in d:
        d[l[i]]=1
print(d)
res=(sum(d.keys())*2)-sum(l)
print(res)
    