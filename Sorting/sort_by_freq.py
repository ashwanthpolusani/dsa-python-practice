def createdict(arr):
    d={}
    for i in arr:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    
    m=max(d.values())
    b=[]
    for i in range(m+1):
        b.append([])
    for tup in d.items():
        b[tup[1]].append(tup[0])
    c=[]
    for i in range(len(b)):
        for j in b[i]:
            c.extend([j]*i)
    return c
arr=[7,2,6,3,6,7,7,2,2,2,9,9,1,1,1]
print(createdict(arr))